from uiautomator import device as d

import unittest, commands

camera_mode = ['Panaroma', 'PerfectShot', 'BurstFast', 'BurstSlow', 'Video', 'HDR', 'Smile', 'Single']

panaroma_settings = ['Geo', 'Exposure', 'ISO']
perfectshot_settings = ['Geo', 'Scenes', 'Exposure']
burst_settings = ['Geo', 'PictureSize', 'Scenes', 'Exposure']
video_settings = ['TestCamera', 'Geo', 'VideoSize', 'Exposure', 'WhiteBalance']
hdr_settings = ['Geo', 'PictureSize', 'SelfTimer']
smile_settings = ['Geo', 'PictureSize', 'Scenes', 'Exposure', 'WhiteBalance', 'ISO']
single_settings = ['TestCamera', 'Hints', 'Geo', 'PictureSize', 'Scenes', 'Exposure', 'WhiteBalance', 'ISO', 'SelfTimer']

testcamera_options = []
hints_options = ['Off', 'On']
geo_options = ['Off', 'On']
picsize_options = ['WideScreen', 'StandardScreen']
scenes_options = ['barcode', 'night-portrait', 'portrait', 'landscape', 'night', 'sports', 'auto']
expo_options = ['-6', '-3', '0', '3', '6']
wb_options = ['cloudy-daylight', 'fluorescent', 'daylight', 'incandescent', 'auto']
iso_options = ['iso-800', 'iso-400', 'iso-200', 'iso-100', 'auto']
selftimer_options = ['0', '3', '5', '10']
videosize_options = ['SD', 'HD', 'HDHS', 'FullHD', 'FullHDHS']

dict_for_panaroma_settings_options = {
    panaroma_settings[0]: geo_options,
    panaroma_settings[1]: expo_options,
    panaroma_settings[2]: iso_options
}

dict_for_perfectshot_settings_options = {
    perfectshot_settings[0]: geo_options,
    perfectshot_settings[1]: scenes_options,
    perfectshot_settings[2]: expo_options
}

dict_for_burst_settings_options = {
    burst_settings[0]: geo_options,
    burst_settings[1]: picsize_options,
    burst_settings[2]: scenes_options,
    burst_settings[3]: expo_options
}

dict_for_video_settings_options = {
    video_settings[0]: testcamera_options,
    video_settings[1]: geo_options,
    video_settings[2]: videosize_options,
    video_settings[3]: expo_options,
    video_settings[3]: wb_options
}

dict_for_hdr_settings_options = {
    hdr_settings[0]: geo_options,
    hdr_settings[1]: picsize_options,
    hdr_settings[2]: selftimer_options,
}

dict_for_smile_settings_options = {
    smile_settings[0]: geo_options,
    smile_settings[1]: picsize_options,
    smile_settings[2]: scenes_options,
    smile_settings[3]: expo_options,
    smile_settings[4]: wb_options,
    smile_settings[5]: iso_options,
}

dict_for_single_settings_options = {
    single_settings[0]: testcamera_options,
    single_settings[1]: hints_options,
    single_settings[2]: geo_options,
    single_settings[3]: picsize_options,
    single_settings[4]: scenes_options,
    single_settings[5]: expo_options,
    single_settings[6]: wb_options,
    single_settings[7]: iso_options,
    single_settings[8]: selftimer_options
}

dict_for_settings = {
    camera_mode[0]: panaroma_settings,
    camera_mode[1]: perfectshot_settings,
    camera_mode[2]: burst_settings,
    camera_mode[3]: burst_settings,
    camera_mode[4]: video_settings,
    camera_mode[5]: hdr_settings,
    camera_mode[6]: smile_settings,
    camera_mode[7]: single_settings
    }

dict_for_options = {
    camera_mode[0]: dict_for_panaroma_settings_options,
    camera_mode[1]: dict_for_perfectshot_settings_options,
    camera_mode[2]: dict_for_burst_settings_options,
    camera_mode[3]: dict_for_burst_settings_options,
    camera_mode[4]: dict_for_video_settings_options,
    camera_mode[5]: dict_for_hdr_settings_options,
    camera_mode[6]: dict_for_smile_settings_options,
    camera_mode[7]: dict_for_single_settings_options
}

dict_for_settings_keys = {
    'Hints': 'pref_camera_hints_key',
    'Geo': 'pref_camera_geo_location_key',
    'PictureSize': 'pref_camera_picture_size_key',
    'Scenes': 'pref_camera_scenemode_key',
    'Exposure': 'pref_camera_exposure_key',
    'WhiteBalance': 'pref_camera_whitebalance_key',
    'ISO': 'pref_camera_iso_key',
    'SelfTimer': 'pref_camera_delay_shooting_key',
    'VideoSize': 'pref_video_quality_key'
}

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
    def tearDown(self):
        super(CameraTest,self).tearDown()
        
    def _setCameraMode(self, mode, setting, option):
        d(description='Camera settings').click.wait()
        print dict_for_settings.get(mode).index(setting)
        if dict_for_settings.get(mode).index(setting) < 7:
            print 'if'
            d(resourceId="com.intel.camera22:id/hori_list_button")[dict_for_settings.get(mode).index(setting)].click.wait()
            print len(dict_for_settings.get(mode))
            print dict_for_options.get(mode).get(setting).index(option)
            if len(dict_for_settings.get(mode)) > 7:
                d(resourceId="com.intel.camera22:id/hori_list_button")[7 + dict_for_options.get(mode).get(setting).index(option)].click.wait()
            else:
                d(resourceId="com.intel.camera22:id/hori_list_button")[len(dict_for_settings.get(mode)) + dict_for_options.get(mode).get(setting).index(option)].click.wait()

        else:
            print 'else'
            # d(resourceId="com.intel.camera22:id/hori_list_button")[6].drag.to(resourceId="com.intel.camera22:id/hori_list_button")[0]
            d.swipe(640,180,100,180,steps=10)
            print dict_for_settings.get(mode).index(setting)
            print len(dict_for_settings.get(mode))
            d(resourceId="com.intel.camera22:id/hori_list_button")[dict_for_settings.get(mode).index(setting) - (len(dict_for_settings.get(mode)) - 7)].click.wait()
            d(resourceId="com.intel.camera22:id/hori_list_button")[7 + dict_for_options.get(mode).get(setting).index(option)].click.wait()
        

        print dict_for_settings_keys.get(setting)
        if setting == 'Geo':
            result = commands.getoutput('adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep ' + dict_for_settings_keys.get(setting))
        else:
            result = commands.getoutput('adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep ' + dict_for_settings_keys.get(setting))
        
        print result
        return result


    def testSetCameraOption(self):
        result = self._setCameraMode('Smile', 'ISO', 'auto')
        assert result.find('iso-auto') != -1, 'failed'




if __name__ == '__main__':  
    unittest.main()


