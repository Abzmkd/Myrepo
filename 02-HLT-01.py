
def calc_glass_required(overall_width, overall_height):
    """overall_width and overall_height are in metres."""
    glass_width = overall_width - 0.0254 - 0.0254
    glass_height = overall_height - 0.0254 - 0.0254
   

    return glass_width * glass_height



overall_width = float(input("Enter width (m): "))

while overall_width < 0.5 or overall_width > 3.5:
    print("Please check your measurement.\nWidth between 0.5 and 3.5m.")
    overall_width = float(input("Enter width (m): "))


overall_height = float(input("Enter height (m): "))

while overall_height < 0.5 or overall_height > 2.0:
    print("Please check your measurement.\nHeight between 0.5 and 2.0m.")
    overall_height = float(input("Enter height (m): "))


glass_required = calc_glass_required(overall_width, overall_height)


top_frame_ft_float = overall_width * 3.281
top_frame_ft = int(top_frame_ft_float)
top_frame_in = (top_frame_ft_float - top_frame_ft) * 12

left_frame_ft_float = (overall_height - 0.0254 - 0.0254) * 3.281
left_frame_ft = int(left_frame_ft_float)
left_frame_in = (left_frame_ft_float - left_frame_ft) * 12


print(f"Glass required is {glass_required} sq. metres")
print(f"Top and bottom {top_frame_ft} and {top_frame_in:3f} inches")
print(f"Left and right {left_frame_ft} and {left_frame_in:3f} inches")