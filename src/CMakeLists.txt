
add_library(pbcvt SHARED python_module.cpp pyboost_cv2_converter.cpp pyboost_cv3_converter.cpp pyboost_cv4_converter.cpp)
set_target_properties(pbcvt PROPERTIES
  PREFIX ""
  LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/python_test
  )
target_link_libraries(pbcvt  ${Boost_LIBRARIES} ${Python3_LIBRARIES} ${OpenCV_LIBRARIES})



add_library(HKIPcamera SHARED pyhk.cpp  HKIPcamera.cpp  pyboost_cv2_converter.cpp pyboost_cv3_converter.cpp pyboost_cv4_converter.cpp)
set_target_properties(HKIPcamera PROPERTIES
  PREFIX ""
  LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/python_test
  )
target_link_libraries(HKIPcamera ${Boost_LIBRARIES} ${Python3_LIBRARIES} ${OpenCV_LIBRARIES}
  # the libs in the directory : CH-HCNetSDKV6.1.6.3_build20200925_Linux64/lib
  # make sure that these .so files are copied to the /usr/lib or /us/local/lib directory!
  libz.so
	libssl.so
	libhpr.so
	libhcnetsdk.so
	libcrypto.so
	libSuperRender.so
	libPlayCtrl.so
	libNPQos.so
	libHCCore.so
	libAudioRender.so
  )




