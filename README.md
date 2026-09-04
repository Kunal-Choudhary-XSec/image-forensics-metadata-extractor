
# 🔍 Image Forensics

A browser-based image metadata and forensic analysis tool that reveals hidden information embedded inside digital images.

Analyze EXIF, GPS, camera information, timestamps, software traces, XMP, IPTC, and other metadata directly in your browser — without uploading the image to a server.

**Privacy-first:** Images are processed locally in the browser and are not sent to a backend server for analysis.

---

## 🌊 What the Project Does

Upload an image and **Image Forensics** extracts available metadata and presents it in an easy-to-understand forensic report.

The analyzer can identify:

- Camera make and model
- Lens information
- Image dimensions
- File name and file size
- Date and time information
- Software/editing traces
- EXIF metadata
- XMP metadata
- IPTC metadata
- GPS coordinates
- Latitude
- Longitude
- Altitude
- And many additional metadata fields

When information is unavailable, the application displays **"Not Found"** instead of inventing or guessing a value.

---

## ✨ Features

- **Deep EXIF analysis** — Extracts 40+ metadata fields from supported images.
- **GPS detection** — Detects embedded latitude, longitude, and altitude information when available.
- **Google Maps integration** — GPS coordinates can be copied or opened directly in Google Maps.
- **Camera detection** — Identifies camera manufacturer and model information stored inside the image.
- **Date & time extraction** — Displays available image creation or modification timestamps.
- **Software fingerprinting** — Detects software/editor information stored in metadata.
- **XMP & IPTC support** — Reads additional metadata beyond standard EXIF information.
- **Privacy-first processing** — Images are analyzed locally inside the browser.
- **Forensic summary** — Provides clear Yes/No indicators for metadata, camera, date/time, and GPS availability.
- **Search & filtering** — Quickly search through extracted metadata fields.
- **Export report** — Generate an exportable forensic report containing the extracted image information.
- **GPS visualization** — Displays detected coordinates on an interactive map.
- **Responsive interface** — Works across desktop and mobile screen sizes.
- **No fake results** — Missing metadata is explicitly shown as unavailable.

---

## 🧪 How an Analysis Works

```text
┌─────────────────┐
│   Upload Image  │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Read Image File │
└────────┬────────┘
         ↓
┌─────────────────────┐
│  Extract Metadata   │
│   EXIF / XMP / IPTC │
└────────┬────────────┘
         ↓
┌─────────────────────┐
│  Analyze Important  │
│ Forensic Indicators │
└────────┬────────────┘
         ↓
┌─────────────────────┐
│ GPS / Camera / Date │
│      Detection      │
└────────┬────────────┘
         ↓
┌─────────────────────┐
│   Forensic Report   │
│   + Map + Metadata  │
└─────────────────────┘
````

Everything happens client-side, so the original image can remain on the user's device during analysis.

---

## 🕵️ Forensic Checks

The application provides four primary forensic indicators:

| Check                  | Purpose                                            |
| ---------------------- | -------------------------------------------------- |
| **Metadata Found**     | Determines whether useful metadata exists          |
| **Camera Detected**    | Checks for camera manufacturer/model information   |
| **Date/Time Found**    | Checks for available timestamp information         |
| **GPS Location Found** | Checks whether geographic coordinates are embedded |

Each result is derived from the actual extracted metadata rather than hard-coded values.

---

## 📍 GPS Analysis

When an image contains GPS information, Image Forensics extracts:

* Latitude
* Longitude
* Altitude

The coordinates can then be:

* Viewed on the map
* Copied to the clipboard
* Opened in Google Maps

If GPS information does not exist, the application clearly reports that it was not found.

---

## 🔐 Privacy

Privacy is one of the core principles of the project.

### Local Processing

```text
User's Image
     │
     ▼
  Browser
     │
     ├── EXIF extraction
     ├── XMP extraction
     ├── IPTC extraction
     ├── GPS extraction
     └── Forensic analysis
```

The image does not need to be uploaded to a remote server for metadata analysis.

This makes the tool useful when analyzing potentially sensitive images.

> **Important:** Metadata itself can contain sensitive information such as GPS coordinates, timestamps, device information, and software details. Users should review metadata before publicly sharing images.

---

## 🛠 Tech Stack

| Layer                 | Technology                            |
| --------------------- | ------------------------------------- |
| **Frontend**          | React + TypeScript                    |
| **Build Tool**        | Vite                                  |
| **Styling**           | Tailwind CSS                          |
| **Metadata Analysis** | Browser-side EXIF metadata extraction |
| **Maps**              | Interactive GPS map                   |
| **Icons**             | Lucide / icon library                 |
| **Deployment**        | Static web hosting                    |

---

## 📁 Project Structure

```text
image-forensics/
│
├── src/
│   ├── components/
│   │   ├── Navbar
│   │   ├── Hero
│   │   ├── Analyzer
│   │   ├── MetadataResults
│   │   ├── ForensicSummary
│   │   ├── GpsMap
│   │   ├── HowItWorks
│   │   └── About
│   │
│   ├── assets/
│   │
│   ├── images/
│   │
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
│
├── public/
│
├── package.json
├── package-lock.json
├── tailwind.config.js
├── vite.config.ts
└── README.md
```

> The exact folder/file names should be adjusted to match the final repository before publishing.

---

## 🚀 Setup

### Prerequisites

You need:

* Node.js
* npm
* A modern web browser

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd image-forensics
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start the Development Server

```bash
npm run dev
```

Then open the application in your browser.

### 🌐 Live Demo

[Image Forensics — Live Demo](https://nightwave-hero-update--kunal46756.replit.app/)

---

## 🖥️ How to Use

### 1. Open Image Forensics

Open the application in your browser.

### 2. Upload an Image

Select a JPG, JPEG, PNG, or other supported image.

### 3. Start Analysis

The application reads the image and extracts available metadata locally.

### 4. Review the Forensic Summary

Check:

* Metadata
* Camera
* Date/Time
* GPS

### 5. Inspect Detailed Metadata

Search and filter through the extracted fields.

### 6. Check GPS Information

If coordinates are available, view the location on the interactive map or open it in Google Maps.

### 7. Export the Report

Use the export functionality to save the forensic analysis.

---

## ⚠️ Limitations

Image Forensics can only extract information that actually exists inside the image.

For example:

```text
Image contains GPS
        ↓
GPS coordinates can be displayed
```

```text
Image contains no GPS
        ↓
GPS Location → Not Found
```

Metadata may also be removed when an image is:

* Screenshot
* Compressed
* Resaved by an application
* Uploaded to certain social media platforms
* Exported through image editing software

Therefore, **absence of metadata does not prove that an image has never been edited.**

---

## 🔎 Example Forensic Information

A single image may reveal information such as:

| Field             | Example     |
| ----------------- | ----------- |
| **File Name**     | `photo.jpg` |
| **Format**        | JPEG        |
| **Dimensions**    | 4000 × 3000 |
| **Camera Make**   | Canon       |
| **Camera Model**  | EOS ...     |
| **Date/Time**     | 2026-...    |
| **GPS Latitude**  | 23.xxxxxx°  |
| **GPS Longitude** | 77.xxxxxx°  |
| **Altitude**      | ...         |
| **Software**      | ...         |

The application displays only information actually extracted from the image.

---

## 🗺️ Project Roadmap

| Phase | Work                          |
| ----: | ----------------------------- |
| **1** | Project setup & image upload  |
| **2** | EXIF metadata extraction      |
| **3** | GPS & camera analysis         |
| **4** | Forensic summary              |
| **5** | Search & filtering            |
| **6** | GPS map integration           |
| **7** | Export report                 |
| **8** | UI polish & responsive design |
| **9** | GitHub documentation          |

---

## 🎯 Future Improvements

Possible future improvements include:

* More advanced image tampering indicators
* Additional metadata formats
* Batch image analysis
* Metadata comparison between images
* Hash generation
* SHA-256 file fingerprinting
* Duplicate image detection
* More detailed forensic reporting
* PDF report generation
* Drag-and-drop upload
* Additional image format support

---

## 🧠 Why This Project?

Digital images often contain information that is invisible when simply viewing the picture.

A photograph can potentially reveal:

* 📷 Camera
* 📅 Date & Time
* 📍 Location
* 💻 Software
* 🗂️ File Information
* 🏷️ Metadata

**Image Forensics** makes this hidden information easier to inspect through a single browser-based interface.

---

## 📜 License

**MIT License** — for educational and research purposes.

````

### Important

The main problem in your original version was **not the content**. It was the Markdown formatting:

- Features were all in one paragraph → now separate bullets.
- Tables were running together → now proper Markdown tables.
- Flowcharts were being interpreted as normal text → now inside ` ```text ` code blocks.
- Project structure was running together → now inside a code block.
- Privacy diagram is also properly separated.
- Setup and usage are now properly numbered sections.

So **replace your current README content with the version above**. It should render cleanly on GitHub.
````
