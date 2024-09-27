# 🗺️ USC Campus Geospatial Analysis Project

This project involves geospatial analysis of key locations across the University of Southern California (USC) campus. Using **OpenLayers**, **Google Earth**, and **PostgreSQL (PostGIS)**, this project visualizes campus landmarks, performs spatial queries, and generates convex hulls and nearest neighbor analyses for the selected points.

## 📍 Features

- **Interactive Map Visualization**: Leveraged OpenLayers to plot various points of interest across the USC campus, such as libraries, cafes, and more.
- **Spatial Database Queries**: Implemented spatial queries with PostgreSQL's PostGIS extension to calculate distances between points and generate convex hulls.
- **Google Earth Integration**: Visualized geospatial data using KML files and Google Earth for enhanced 3D mapping of the USC campus.
  
## 🚀 Project Breakdown

### 1. **OpenLayers Map Visualization**
   - Developed an interactive map with markers representing significant locations on the USC campus.
   - Example locations include **Hahn Central Plaza Fountain**, **USC Law School**, **Panda Express**, and more.
   - Map dynamically renders markers based on geographic coordinates provided in the `OpenLayers` script.
   - Visual representation powered by OpenStreetMap (OSM) and OpenLayers API.

### 2. **PostgreSQL (PostGIS) Spatial Queries**
   - Configured a spatial database with PostGIS to store campus landmarks.
   - Ran convex hull queries to determine the perimeter of all points combined, visualizing the boundary of the points.
   - Performed nearest neighbor analysis to find the closest locations to a given point on campus.

### 3. **Google Earth KML Visualization**
   - Imported KML files to Google Earth for 3D visualization of the selected locations.
   - Created a spirograph pattern of campus points, which can be viewed interactively in Google Earth.
   - Added layers to analyze convex hulls and spatial proximity of various points.

## 🧑‍💻 Technologies Used
- **OpenLayers**: For interactive web mapping and visualization.
- **PostgreSQL + PostGIS**: For managing spatial data and running geographical queries.
- **Google Earth**: For visualizing KML files and performing 3D analysis of spatial data.

## 📊 PostgreSQL Queries
The following PostgreSQL spatial queries were used:
- **Convex Hull Query**: To compute the boundary surrounding all points.
- **Nearest Neighbor Query**: To find the closest landmarks to a reference point.
