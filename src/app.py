import cv2
import requests
import json
import numpy as np

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
API_URL_ANALYZE = "https://api.spoonacular.com/food/images/analyze"
API_URL_NUTRITION = "https://api.spoonacular.com/recipes/guessNutrition"

frame_global = None

def capture_image(filename='food.jpg'):
    global frame_global

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Error: Could not open camera.")

    cv2.namedWindow('Press Mouse Button to Capture', cv2.WINDOW_NORMAL)

    cv2.setMouseCallback('Press Mouse Button to Capture', lambda event, x, y, flags, param: capture_callback(event, x, y, flags, param, frame_global))

    while True:
        ret, frame = cap.read()
        if not ret:
            raise RuntimeError("Failed to grab frame.")
        frame_global = frame
        cv2.imshow('Press Mouse Button to Capture', frame)
        key = cv2.waitKey(1)
        if key & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyallwindows()

    return filename

def capture_callback(event, x, y, flags, param, frame):
    global frame_global
    if event == cv2.EVENT_LBUTTONDOWN:
        filename = 'food.jpg'
        cv2.imwrite(filename, frame)
        food_data = recognize_food(filename)
        food_name = food_data.get('category', {}).get('name')
        if not food_name:
            print("Could not recognize food.")
            return

        print(f"Recognized Food: {food_name}")

        nutrition_info = get_nutrition_info(food_name)
        calories = nutrition_info.get('calories', {}).get('value')
        if calories:
            print(f"Calories: {calories}")
        else:
            print("Could not get calorie information.")

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
        numpy_horizontal_concat = np.concatenate((frame, grey_3_channel), axis=1)
        cv2.putText(numpy_horizontal_concat, f"Recognized Food: {food_name}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(numpy_horizontal_concat, f"Calories: {calories}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow('Result', numpy_horizontal_concat)

def recognize_food(image_path):
    headers = {
        "x-api-key": API_KEY
    }

    files = {'file': open(image_path, 'rb')}

    response = requests.post(
        API_URL_ANALYZE,
        headers=headers,
        files=files
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"Error: {response.status_code}")

def get_nutrition_info(food_name):
    params = {"title": food_name, "apiKey": API_KEY}
    response = requests.get(API_URL_NUTRITION, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(f"Error: {response.status_code}")

def main():
    try:
        capture_image()
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
