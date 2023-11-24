import cv2
import numpy as np

def calculate_average_color(image):
    average_color_per_row = np.average(image, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    return average_color

def calculate_delta_e(cielab1, cielab2):
    delta_e = np.sqrt(np.sum((cielab1 - cielab2) ** 2))
    return delta_e

# Bilder laden
image1 = cv2.imread('Red1.png')
image2 = cv2.imread('Orange.png')
#image2 = cv2.imread('Red2.png')
#image2 = cv2.imread('Red1.png')

# Bilder in CIELab konvertieren
image1_lab = cv2.cvtColor(image1, cv2.COLOR_BGR2Lab)
image2_lab = cv2.cvtColor(image2, cv2.COLOR_BGR2Lab)

# Durchschnittliche Farbwerte berechnen
average_color1 = calculate_average_color(image1_lab)
average_color2 = calculate_average_color(image2_lab)

# Delta E berechnen
delta_e = calculate_delta_e(average_color1, average_color2)

# Bilder nebeneinander anzeigen
combined_image = np.hstack((image1, image2))
cv2.putText(combined_image, f"Delta E: {delta_e:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow('Bildvergleich', combined_image)

# Warte auf Tastendruck, um das Fenster zu schließen
cv2.waitKey(0)
cv2.destroyAllWindows()
