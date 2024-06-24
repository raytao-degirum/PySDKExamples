#
# hand_face_person_detection_parallel_video_stream.py: Multi-Model AI Inference on Video Streams
#
# Copyright DeGirum Corporation 2023
# All rights reserved
#
# This script performs AI inference on a video stream using multiple detection models for hands, faces, and persons. It displays the video with annotated results. The script requires a YAML configuration file as input, which specifies the hardware location for running inference, the model zoo URL, the names of the models for hand, face, and person detection, and the source of the video.
#
# Parameters:
# - hw_location (str): Specifies where to run inference with options '@cloud' for DeGirum cloud, '@local' for local machine, or an IP address for AI server inference.
# - model_zoo_url (str): Provides the URL or path for the model zoo with options 'cloud_zoo_url' for various inference options, '' for AI server serving models from a local folder, or a path to a JSON file for a single model zoo in case of @local inference.
# - hand_det_model_name (str): Specifies the name of the model for hand detection.
# - face_det_model_name (str): Specifies the name of the model for face detection.
# - person_det_model_name (str): Specifies the name of the model for person detection.
# - video_source: Defines the source of the video for inference with options being a camera index for local camera, a URL of an RTSP stream, a URL of a YouTube video, or a path to a video file (e.g., mp4).
#
# The script uses the 'degirum' and 'degirum_tools' modules to connect to the AI inference engine, load the specified models, and perform inference on the provided video source.
#
# Usage:
# python hand_face_person_detection_parallel_video_stream.py --config path/to/config.yaml
#

import yaml
import argparse
import degirum as dg
import degirum_tools

if __name__ == "__main__":
    # Get configuration data from configuration yaml file
    parser = argparse.ArgumentParser(description="Parse YAML file.")
    parser.add_argument(
        "--config", help="Path to the YAML configuration file", required=True
    )
    args = parser.parse_args()
    with open(args.config, "r") as file:
        config_data = yaml.safe_load(file)

    # Set all config options
    hw_location = config_data["hw_location"]
    face_det_model_zoo_url = config_data["face_det_model_zoo_url"]
    face_det_model_name = config_data["face_det_model_name"]
    hand_det_model_zoo_url = config_data["hand_det_model_zoo_url"]
    hand_det_model_name = config_data["hand_det_model_name"]
    person_det_model_zoo_url = config_data["person_det_model_zoo_url"]
    person_det_model_name = config_data["person_det_model_name"]
    video_source = config_data["video_source"]
    overlay_color = [(255, 255, 0), (0, 255, 0), (255, 0, 0)]

    # Load face detection, hand detection models, and person detection models
    face_det_model = dg.load_model(
        model_name=face_det_model_name,
        inference_host_address=hw_location,
        zoo_url=face_det_model_zoo_url,
        token=degirum_tools.get_token(),
    )
    hand_det_model = dg.load_model(
        model_name=hand_det_model_name,
        inference_host_address=hw_location,
        zoo_url=hand_det_model_zoo_url,
        token=degirum_tools.get_token(),
    )
    person_det_model = dg.load_model(
        model_name=person_det_model_name,
        inference_host_address=hw_location,
        zoo_url=person_det_model_zoo_url,
        token=degirum_tools.get_token(),
    )
    person_det_model.overlay_color = overlay_color
    # Create a compound model that combines the three models
    combined_model = degirum_tools.CombiningCompoundModel(
        degirum_tools.CombiningCompoundModel(hand_det_model, face_det_model),
        person_det_model,
    )

    # run AI inference on video stream
    inference_results = degirum_tools.predict_stream(combined_model, video_source)

    # display inference results
    # Press 'x' or 'q' to stop
    with degirum_tools.Display("Hands, Faces and Persons") as display:
        for inference_result in inference_results:
            display.show(inference_result)
