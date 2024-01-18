# import matplotlib.pyplot as plt
#
#
# # Function to display an image and capture the click event to get coordinates
# def get_coordinates(image_path):
#     """
#     Open an image and allow user to click on the image to get coordinates.
#
#     :param image_path: Path to the image file.
#     """
#     # Open the image file
#     img = plt.imread(image_path)
#
#     # Show the image
#     plt.imshow(img)
#     plt.axis('on')  # Show the axis, which includes the scale
#
#     # Function to handle the click event
#     def onclick(event):
#         ix, iy = event.xdata, event.ydata
#         coords = (ix, iy)
#         print(f"Coordinates at cursor: {coords}")
#         plt.annotate(f'({int(ix)}, {int(iy)})', (ix, iy), textcoords="offset points", xytext=(-15, 10), ha='center')
#         plt.scatter([ix], [iy], c='red', s=100)  # Mark the clicked point for visibility
#         plt.show()
#
#     # Connect the click event to the handler function
#     cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)
#
#     plt.show()
#
#
# # Path to the uploaded template image
# template_image_path = r'C:\Nitish\Arc_Flash\Arc_Flash.png'
#
# # Call the function to get coordinates
# get_coordinates(template_image_path)
#-------------------------------------------Sticker Print--------------------------------------------------------------

# import pandas as pd
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
#
# # Function to add new text to an image
# def add_text(image_path, text_positions, values, output_path, font_size):
#     with Image.open(image_path) as img:
#         draw = ImageDraw.Draw(img)
#         font_path = "C:\\Windows\\Fonts\\Arial.ttf"  # Make sure this path is correct
#         font = ImageFont.truetype(font_path, font_size)
#
#         # Check if the 'textsize' method is available
#         if not hasattr(draw, 'textsize'):
#             raise AttributeError("The 'textsize' method is not available in 'ImageDraw' object. "
#                                  "Please ensure that Pillow is installed correctly.")
#
#         # Add new text over the image
#         for label, position in text_positions.items():
#             value_to_write = values[label]  # Access the value using the label as a key
#             text_width, text_height = draw.textsize(str(value_to_write), font=font)
#             position = (position[0], position[1] - text_height)
#             draw.text(position, str(value_to_write), font=font, fill="black")
#
#         img.save(output_path)
#
#     return output_path
# # Function to add new text to an image
# def add_text(image_path, text_positions, values, output_path, font_size):
#     with Image.open(image_path) as img:
#         draw = ImageDraw.Draw(img)
#         font_path = "C:\\Windows\\Fonts\\Arial.ttf"  # Make sure this path is correct
#         font = ImageFont.truetype(font_path, font_size)
#
#         # Add new text over the image
#         for label, position in text_positions.items():
#             value_to_write = values[label]  # Access the value using the label as a key
#             text_width, text_height = draw.textsize(str(value_to_write), font=font)
#             position = (position[0], position[1] - text_height)
#             draw.text(position, str(value_to_write), font=font, fill="black")
#
#         img.save(output_path)
#
#     return output_path
#
# # Load the Excel file
# excel_path = r'C:\Nitish\Arc_Flash\Test Arc Flash.xlsx'  # Correct path to the Excel file
# data = pd.read_excel(excel_path)  # Assuming there are no headers in the Excel file
#
# # Use iloc to access the value by position (assuming no headers)
# values = {
#     "Shock Hazard-Cover Removed": data.iloc[0, 0],  # Access by index if no headers
#     "Arc Fault Current": data.iloc[0, 1],
#     "Working Distance Covered": data.iloc[0, 2],
#     "Incident Energy": data.iloc[0, 3]
# }
#
# # Define the coordinates for the text positions
# text_positions = {
#     "Shock Hazard-Cover Removed": (555, 154),
#     "Arc Fault Current": (555, 178),
#     "Working Distance Covered": (555, 201),
#     "Incident Energy": (555, 227)
# }
#
# # Define the font size
# font_size = 16  # Adjust as needed
#
# # Path to your blank template image
# template_image_path = r'C:\Nitish\Arc_Flash\Arc Flash_Blank.png'  # Correct path to the template image
#
# # Path for the output image
# output_image_path = r'C:\Nitish\Arc_Flash\image.png'  # Correct path for the output image
#
# # Call the function to add new text to the image
# updated_image_path = add_text(
#     template_image_path,
#     text_positions,
#     values,
#     output_image_path,
#     font_size
# )
#
# print(f"Updated image saved at: {updated_image_path}")
