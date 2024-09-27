import math

def generate_spirograph_points(R, r, a, num_loops, lon_center, lat_center):
    points = []
    num_iterations = int(num_loops * (R / math.gcd(R, r)) * 2 * math.pi / 0.01)

    for i in range(num_iterations):
        t = i * 0.01
        x = (R - r) * math.cos(t) + a * math.cos((R - r) * t / r)
        y = (R - r) * math.sin(t) - a * math.sin((R - r) * t / r)

        scaling_factor = 0.0001
        lon = x * scaling_factor + lon_center
        lat = y * scaling_factor + lat_center
        points.append((lon, lat))
    return points

def create_kml(points, file_name, lon_center, lat_center):
    kml_header = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
    kml_footer = '</Document>\n</kml>'
    red_dotted_line_style = '''
  <Style id="redDottedLineStyle">
    <LineStyle>
      <color>ff0000ff</color>
      <width>4</width>
      <gx:labelVisibility>1</gx:labelVisibility>
      <gx:physicalWidth>3</gx:physicalWidth>
      <gx:physicalOffset>3</gx:physicalOffset>
    </LineStyle>
  </Style>
'''

    location_icon_style = '''
  <Style id="locationIconStyle">
    <IconStyle>
      <Icon>
        <href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href>
      </Icon>
      <hotSpot x="0.5" y="1" xunits="fraction" yunits="fraction"/>
    </IconStyle>
  </Style>
'''
    
    kml_content = [kml_header, red_dotted_line_style, location_icon_style]
    
    coordinates = "\n".join([f"{lon},{lat},0" for lon, lat in points])
    line_string = f'''
  <Placemark>
    <name>Spirograph Pattern</name>
    <styleUrl>#redDottedLineStyle</styleUrl>
    <LineString>
      <tessellate>1</tessellate>
      <coordinates>
{coordinates}
      </coordinates>
    </LineString>
  </Placemark>
'''

    location_icon = f'''
  <Placemark>
    <name>Center Location</name>
    <styleUrl>#locationIconStyle</styleUrl>
    <Point>
      <coordinates>{lon_center},{lat_center},0</coordinates>
    </Point>
  </Placemark>
'''

    kml_content.extend([line_string, location_icon, kml_footer])

    with open(file_name, 'w') as file:
        file.writelines(kml_content)

R, r, a, num_loops = 36, 9, 30, 4
lon_center, lat_center = -118.28548350733348, 34.020743920886055

points = generate_spirograph_points(R, r, a, num_loops, lon_center, lat_center)
kml_file_name = 'Vedant_Spirograph.kml'
create_kml(points, kml_file_name, lon_center, lat_center)

print(f"Created KML file with spirograph pattern and center location icon.")

