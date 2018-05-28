#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse
import struct
import imghdr
import random
import json
import hashlib
import hmac
import requests
import urllib
import uuid
import time
from datetime import datetime
import calendar
from requests_toolbelt import MultipartEncoder
import dill
from database.models import InstagramUser

# Turn off InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_image_size(filename):
  with open(filename, 'rb') as fhandle:
    head = fhandle.read(24)
    if len(head) != 24:
      raise RuntimeError("Invalid Header")
    if imghdr.what(filename) == 'png':
      check = struct.unpack('>i', head[4:8])[0]
      if check != 0x0d0a1a0a:
        raise RuntimeError("PNG: Invalid check")
      width, height = struct.unpack('>ii', head[16:24])
    elif imghdr.what(filename) == 'gif':
      width, height = struct.unpack('<HH', head[6:10])
    elif imghdr.what(filename) == 'jpeg':
      fhandle.seek(0)  # Read 0xff next
      size = 2
      ftype = 0
      while not 0xc0 <= ftype <= 0xcf:
        fhandle.seek(size, 1)
        byte = fhandle.read(1)
        while ord(byte) == 0xff:
          byte = fhandle.read(1)
        ftype = ord(byte)
        size = struct.unpack('>H', fhandle.read(2))[0] - 2
      # We are at a SOFn block
      fhandle.seek(1, 1)  # Skip `precision' byte.
      height, width = struct.unpack('>HH', fhandle.read(4))
    else:
      raise RuntimeError("Unsupported format")
    return width, height


class InstagramAPI:
  API_URL = 'https://i.instagram.com/api/v1/'
  DEVICE_SETTINTS = {'manufacturer': 'Xiaomi', 'model': 'HM 1SW', 'android_version': 18, 'android_release': '4.3'}
  USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(
    **DEVICE_SETTINTS)
  IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
  EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on' ''
  SIG_KEY_VERSION = '4'

  # username            # Instagram username
  # password            # Instagram password
  # debug               # Debug
  # uuid                # UUID
  # device_id           # Device ID
  # username_id         # Username ID
  # token               # _csrftoken
  # is_logged_in        # Session status
  # rank_token          # Rank token

  def __init__(self, instagram_user):
    m = hashlib.md5()
    m.update(instagram_user.username.encode('utf-8') + instagram_user.password.encode('utf-8'))
    self.device_id = self.generate_device_id(m.hexdigest())
    self.set_user(instagram_user.username, instagram_user.password)
    self.is_logged_in = False
    self.last_response = None
    self.s = requests.Session()
    self.instagram_user = instagram_user

  def set_user(self, username, password):
    self.username = username
    self.password = password
    self.uuid = self.generateUUID(True)

  def login(self, force=False):
    if (not self.is_logged_in or force):

      if self.instagram_user.login_session and self.instagram_user.username_id and not force:
        last_cookies = self.instagram_user.login_session
        self.username_id = self.instagram_user.username_id
        self.is_logged_in = True
        self.token = last_cookies["csrftoken"]
        self.s.cookies.update(self.instagram_user.login_session)

      elif self.send_request('si/fetch_headers/?challenge_type=signup&guid=' + self.generateUUID(False), None, True):

        data = {
          'phone_id': self.generateUUID(True),
          '_csrftoken': self.last_response.cookies['csrftoken'],
          'username': self.username,
          'guid': self.uuid,
          'device_id': self.device_id,
          'password': self.password,
          'login_attempt_count': '0'
        }

        if self.send_request('accounts/login/', self.generate_signature(json.dumps(data)), True):
          print("LOGGED IN")
          self.is_logged_in = True
          self.username_id = self.last_json["logged_in_user"]["pk"]
          self.rank_token = "%s_%s" % (self.username_id, self.uuid)
          self.token = self.last_response.cookies["csrftoken"]

          self.sync_features()
          self.autocomplete_user_list()
          self.timeline_feed()
          self.get_v2_inbox()
          self.get_recent_activity()

          self.instagram_user.login_session = requests.utils.dict_from_cookiejar(self.s.cookies)
          self.instagram_user.username_id = self.username_id
          self.instagram_user.save()

          return True

  def sync_features(self):
    data = json.dumps({
      '_uuid': self.uuid,
      '_uid': self.username_id,
      'id': self.username_id,
      '_csrftoken': self.token,
      'experiments': self.EXPERIMENTS
    })
    return self.send_request('qe/sync/', self.generate_signature(data))

  def autocomplete_user_list(self):
    return self.send_request('friendships/autocomplete_user_list/')

  def timeline_feed(self):
    return self.send_request('feed/timeline/')

  def megaphone_log(self):
    return self.send_request('megaphone/log/')

  def expose(self):
    data = json.dumps({
      '_uuid': self.uuid,
      '_uid': self.username_id,
      'id': self.username_id,
      '_csrftoken': self.token,
      'experiment': 'ig_android_profile_contextual_feed'
    })
    return self.send_request('qe/expose/', self.generate_signature(data))

  def logout(self):
    self.send_request('accounts/logout/')

  def upload_photo(self, photo, caption=None, upload_id=None, is_sidecar=None, is_story=None):
    if upload_id is None:
      upload_id = str(int(time.time() * 1000))
    data = {
      'upload_id':
        upload_id,
      '_uuid':
        self.uuid,
      '_csrftoken':
        self.token,
      'image_compression':
        '{"lib_name":"jt","lib_version":"1.3.0","quality":"87"}',
      'photo': ('pending_media_%s.jpg' % upload_id, open(photo, 'rb'), 'application/octet-stream', {
        'Content-Transfer-Encoding': 'binary'
      })
    }
    if is_sidecar:
      data['is_sidecar'] = '1'
    m = MultipartEncoder(data, boundary=self.uuid)
    self.s.headers.update({
      'X-IG-Capabilities': '3Q4=',
      'X-IG-Connection-Type': 'WIFI',
      'Cookie2': '$Version=1',
      'Accept-Language': 'en-US',
      'Accept-Encoding': 'gzip, deflate',
      'Content-type': m.content_type,
      'Connection': 'close',
      'User-Agent': self.USER_AGENT
    })
    response = self.s.post(self.API_URL + "upload/photo/", data=m.to_string())
    if response.status_code == 200:
      if self.configure(upload_id, photo, caption, is_story=is_story) and not is_story:
        self.expose()
    return False

  def upload_album(self, media, caption=None):
    if not media:
      raise Exception("List of media to upload can't be empty.")

    if len(media) < 2 or len(media) > 10:
      raise Exception('Instagram requires that albums contain 2-10 items. You tried to submit {}.'.format(len(media)))

    # Figure out the media file details for ALL media in the album.
    # NOTE: We do this first, since it validates whether the media files are
    # valid and lets us avoid wasting time uploading totally invalid albums!
    for idx, item in enumerate(media):
      if not item.get('file', '') or item.get('tipe', ''):
        raise Exception('Media at index "{}" does not have the required "file" and "type" keys.'.format(idx))

      # $item_internal_metadata = new InternalMetadata();
      # If usertags are provided, verify that the entries are valid.
      if item.get('usertags', []):
        self.throw_if_invalid_usertags(item['usertags'])

      # Pre-process media details and throw if not allowed on Instagram.
      if item.get('type', '') == 'photo':
        # Determine the photo details.
        # $item_internal_metadata->setPhotoDetails(Constants::FEED_TIMELINE_ALBUM, $item['file']);
        pass

      else:
        raise Exception('Unsupported album media type "{}".'.format(item['type']))

      item_internal_metadata = {}
      item['internalMetadata'] = item_internal_metadata

    # Perform all media file uploads.
    for idx, item in enumerate(media):
      item_internal_metadata = item['internalMetadata']
      item_upload_id = self.generate_upload_id()
      if item.get('type', '') == 'photo':
        self.upload_photo(item['file'], caption=caption, is_sidecar=True, upload_id=item_upload_id)

      item['internalMetadata']['upload_id'] = item_upload_id

    return self.configure_timeline_album(media, captionText=caption)

  def upload_story_photo(self, photo):
    return self.upload_photo(photo, is_story=True)

  def throw_if_invalid_usertags(self, usertags):
    for user_position in usertags:
      # Verify this usertag entry, ensuring that the entry is format
      # ['position'=>[0.0,1.0],'user_id'=>'123'] and nothing else.
      correct = True
      if isinstance(user_position, dict):
        position = user_position.get('position', None)
        user_id = user_position.get('user_id', None)

        if isinstance(position, list) and len(position) == 2:
          try:
            x = float(position[0])
            y = float(position[1])
            if x < 0.0 or x > 1.0:
              correct = False
            if y < 0.0 or y > 1.0:
              correct = False
          except:
            correct = False
        try:
          user_id = int(user_id)
          if user_id < 0:
            correct = False
        except:
          correct = False
      if not correct:
        raise Exception('Invalid user entry in usertags array.')

  def configure_timeline_album(self, media, captionText=''):
    endpoint = 'media/configure_sidecar/'
    album_upload_id = self.generate_upload_id()

    date = datetime.utcnow().isoformat()
    children_metadata = []
    for item in media:
      item_internal_metadata = item['internalMetadata']
      upload_id = item_internal_metadata.get('upload_id', self.generate_upload_id())
      if item.get('type', '') == 'photo':
        # Build this item's configuration.
        photo_config = {
          'date_time_original': date,
          'scene_type': 1,
          'disable_comments': False,
          'upload_id': upload_id,
          'source_type': 0,
          'scene_capture_type': 'standard',
          'date_time_digitized': date,
          'geotag_enabled': False,
          'camera_position': 'back',
          'edits': {
            'filter_strength': 1,
            'filter_name': 'IGNormalFilter'
          }
        }
        # This usertag per-file EXTERNAL metadata is only supported for PHOTOS!
        if item.get('usertags', []):
          # NOTE: These usertags were validated in Timeline::upload_album.
          photo_config['usertags'] = json.dumps({'in': item['usertags']})

        children_metadata.append(photo_config)

    # Build the request...
    data = {
      '_csrftoken': self.token,
      '_uid': self.username_id,
      '_uuid': self.uuid,
      'client_sidecar_id': album_upload_id,
      'caption': captionText,
      'children_metadata': children_metadata
    }
    self.send_request(endpoint, self.generate_signature(json.dumps(data)))
    response = self.last_response
    if response.status_code == 200:
      self.last_response = response
      self.last_json = json.loads(response.text)
      return True
    else:
      print("Request return " + str(response.status_code) + " error!")
      self.last_response = response
      self.last_json = json.loads(response.text)
      return False

  def configure(self, upload_id, photo, caption='', is_story=None):
    (w, h) = get_image_size(photo)
    data_dict = {
      '_csrftoken': self.token,
      '_uid': self.username_id,
      '_uuid': self.uuid,
      'device': self.DEVICE_SETTINTS,
      'edits': {
        'crop_original_size': [w * 1.0, h * 1.0],
        'crop_center': [0.0, 0.0],
        'crop_zoom': 1.0
      },
      'extra': {
        'source_width': w,
        'source_height': h,
      }
    }

    if is_story:
      data_dict.update({
        'client_shared_at': str(int(time.time())),
        'source_type': 3,
        'configure_mode': 1,
        'client_timestamp': str(int(time.time()) - random.randint(3, 10)),
        'upload_id': upload_id,
      })
    else:
      data_dict.update({
        'caption': caption,
        'source_type': 4,
        'media_folder': 'Camera',
        'upload_id': upload_id,
      })
    data = json.dumps(data_dict)
    if is_story:
      return self.send_request('media/configure_to_story/?', self.generate_signature(data))
    else:
      return self.send_request('media/configure/?', self.generate_signature(data))

  def edit_media(self, mediaId, captionText=''):
    data = json.dumps({
      '_uuid': self.uuid,
      '_uid': self.username_id,
      '_csrftoken': self.token,
      'caption_text': captionText
    })
    return self.send_request('media/' + str(mediaId) + '/edit_media/', self.generate_signature(data))

  def remove_self_tag(self, mediaId):
    data = json.dumps({'_uuid': self.uuid, '_uid': self.username_id, '_csrftoken': self.token})
    return self.send_request('media/' + str(mediaId) + '/remove/', self.generate_signature(data))

  def media_info(self, mediaId):
    data = json.dumps({'_uuid': self.uuid, '_uid': self.username_id, '_csrftoken': self.token, 'media_id': mediaId})
    return self.send_request('media/' + str(mediaId) + '/info/', self.generate_signature(data))

  def delete_media(self, mediaId, media_type=1):
    data = json.dumps({
      '_uuid': self.uuid,
      '_uid': self.username_id,
      '_csrftoken': self.token,
      'media_type': media_type,
      'media_id': mediaId
    })
    return self.send_request('media/' + str(mediaId) + '/delete/', self.generate_signature(data))

  def get_profile_data(self):
    data = json.dumps({'_uuid': self.uuid, '_uid': self.username_id, '_csrftoken': self.token})
    return self.send_request('accounts/current_user/?edit=true', self.generate_signature(data))

  def get_story(self, usernameId):
    return self.send_request('feed/user/' + str(usernameId) + '/reel_media/')

  def get_recent_activity(self):
    activity = self.send_request('news/inbox/?')
    return activity

  def get_following_recent_activity(self):
    activity = self.send_request('news/?')
    return activity

  def get_v2_inbox(self):
    inbox = self.send_request('direct_v2/inbox/?')
    return inbox

  def get_v2_threads(self, thread, cursor=None):
    endpoint = 'direct_v2/threads/{0}'.format(thread)
    if cursor is not None:
      endpoint += '?cursor={0}'.format(cursor)
    inbox = self.send_request(endpoint)
    return inbox

  def getUserTags(self, usernameId):
    tags = self.send_request(
      'usertags/' + str(usernameId) + '/feed/?rank_token=' + str(self.rank_token) + '&ranked_content=true&')
    return tags

  def getSelfUserTags(self):
    return self.getUserTags(self.username_id)

  def tag_feed(self, tag):
    userFeed = self.send_request(
      'feed/tag/' + str(tag) + '/?rank_token=' + str(self.rank_token) + '&ranked_content=true&')
    return userFeed

  def get_timeline(self):
    query = self.send_request('feed/timeline/?rank_token=' + str(self.rank_token) + '&ranked_content=true&')
    return query

  def get_hashtag_feed(self, hashtagString, maxid=''):
    return self.send_request('feed/tag/' + hashtagString + '/?max_id=' + str(maxid) + '&rank_token=' + self.rank_token +
                             '&ranked_content=true&')

  def search_location(self, query):
    location_feed = self.send_request('fbsearch/places/?rank_token=' + str(self.rank_token) + '&query=' + str(query))
    return location_feed

  def getPendingFollowRequests(self):
    return self.send_request('friendships/pending?')

  def ignore(self, userId):
    data = json.dumps({'_uuid': self.uuid, '_uid': self.username_id, 'user_id': userId, '_csrftoken': self.token})
    return self.send_request('friendships/ignore/' + str(userId) + '/', self.generate_signature(data))

  def generate_signature(self, data, skip_quote=False):
    if not skip_quote:
      try:
        parsedData = urllib.parse.quote(data)
      except AttributeError:
        parsedData = urllib.quote(data)
    else:
      parsedData = data
    return 'ig_sig_key_version=' + self.SIG_KEY_VERSION + '&signed_body=' + hmac.new(
      self.IG_SIG_KEY.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest() + '.' + parsedData

  def generate_device_id(self, seed):
    volatile_seed = "12345"
    m = hashlib.md5()
    m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
    return 'android-' + m.hexdigest()[:16]

  def generateUUID(self, type):
    generated_uuid = str(uuid.uuid4())
    if type:
      return generated_uuid
    else:
      return generated_uuid.replace('-', '')

  def generate_upload_id(self):
    return str(calendar.timegm(datetime.utcnow().utctimetuple()))

  def send_request(self, endpoint, post=None, login=False):
    verify = False  # don't show request warning

    if (not self.is_logged_in and not login):
      self.login(force=True)

    self.s.headers.update({
      'Connection': 'close',
      'Accept': '*/*',
      'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'Cookie2': '$Version=1',
      'Accept-Language': 'en-US',
      'User-Agent': self.USER_AGENT
    })

    while True:
      try:
        if post:
          response = self.s.post(self.API_URL + endpoint, data=post, verify=verify)
        else:
          response = self.s.get(self.API_URL + endpoint, verify=verify)
        break
      except Exception as e:
        print('Except on send_request (wait 10 sec and resend): ' + str(e))
        time.sleep(10)

    if response.status_code == 200:
      self.last_response = response
      self.last_json = json.loads(response.text)
      return True
    else:
      self.last_response = response
      self.last_json = json.loads(response.text)
      if 'error_type' in self.last_json and self.last_json['error_type'] == 'sentry_block':
        self.last_json = {"error": "ACCOUNT POSSIBLY GOT BANNED BY INSTAGRAM"}

      elif "message" in self.last_json and self.last_json["message"] == "login_required":
        # means we aren't logged in, try to login
        self.is_logged_in = False
        self.instagram_user.login_session = ""
        self.instagram_user.save()
        return self.send_request(endpoint, post=post)

      else:
        self.last_json = {"error": "Request failed with " + str(response.status_code)}
