from PIL import Image
from PIL.ExifTags import TAGS
import exifread


# ===== IMAGE FILE =====
image_path = "IMG_20260620_155548.jpg"


# ===== BASIC IMAGE INFO =====
image = Image.open(image_path)

print("=" * 50)
print("        IMAGE FORENSICS REPORT")
print("=" * 50)

print(f"\nFile Name      : {image_path}")
print(f"Format         : {image.format}")
print(f"Resolution     : {image.width} x {image.height}")
print(f"Color Mode     : {image.mode}")


# ===== EXIF DATA =====
exif_data = image.getexif()

make = "Not Found"
model = "Not Found"
datetime = "Not Found"
software = "Not Found"

for tag_id, value in exif_data.items():
    tag = TAGS.get(tag_id, tag_id)

    if tag == "Make":
       make = value

    elif tag == "Model":
        model = value

    elif tag == "DateTime":
        datetime = value

    elif tag == "Software":
        software = value

print("\nPHONE INFORMATION")
print("-" * 50)

print(f"Brand          : {make}")
print(f"Model          : {model}")
print(f"Software       : {software}")
print(f"Date Taken     : {datetime}")


# ===== GPS EXTRACTION =====
print("\nGPS INFORMATION")
print("-" * 50)

with open(image_path, "rb") as f:
    tags = exifread.process_file(f)

try:
    lat_ref = str(tags["GPS GPSLatitudeRef"])
    lat = tags["GPS GPSLatitude"].values

    lon_ref = str(tags["GPS GPSLongitudeRef"])
    lon = tags["GPS GPSLongitude"].values

    altitude = tags.get("GPS GPSAltitude", "Unknown")

    # Convert to decimal
    latitude = (
        float(lat[0])
        + float(lat[1]) / 60
        + float(lat[2]) / 3600
    )

    longitude = (
        float(lon[0])
        + float(lon[1]) / 60
        + float(lon[2]) / 3600
    )

    if lat_ref == "S":
        latitude = -latitude

    if lon_ref == "W":
        longitude = -longitude

    print(f"Latitude       : {latitude:.6f}")
    print(f"Longitude      : {longitude:.6f}")
    print(f"Altitude       : {altitude}")

    print("\nGoogle Maps:")
    print(
        f"https://maps.google.com/?q={latitude:.6f},{longitude:.6f}"
    )

except:
    print("GPS Location   : Not Available")

print("\n" + "=" * 50)
print("          REPORT GENERATED")
print("=" * 50)