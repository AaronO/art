colors = ximport( "colors" )

font( "Helvetica", 200 )
align( CENTER )
text_path_line_1 = textpath( "Noise", 0, 200, width = WIDTH)
text_path_line_2 = textpath( "to", 0, 400, width = WIDTH)
text_path_line_3 = textpath( "Signal", 0, 600, width = WIDTH)
text_paths = [text_path_line_1, text_path_line_2, text_path_line_3]

resx = 200
resy = 80
rx = 2.0
ry = 1.5
dotsize = 5.5
dx = WIDTH  / float( resx )
dy = HEIGHT / float( resy )

def draw_text() :
    nofill()
    strokewidth( random( 0.2, 2.8 ) )
    clr = choice( [ colors.hex( "#FF0000" ), colors.hex( "#FF0033" ), colors.hex( "#000000" ), colors.hex( "#FF0011" ), colors.hex( "#000000" ) ]   )
    clr.a = random( 0.6, 1 )
    stroke( clr )
    oval( pointx + random( -rx, rx ), pointy + random( -ry, ry ), size, size )
    """
    clr = choice( [ colors.hex( "#FF0000" ), colors.hex( "#FF0033" ), colors.hex( "#000000" ), colors.hex( "#FF0011" ), colors.hex( "#000000" ) ]   )
    clr.a = random( 0.6, 1 )
    stroke( clr )
    oval( pointx + random( -rx, rx ), pointy + random( -ry, ry ), size, size )
    """

for x, y in grid( resx, resy ) : 
    size = choice( [ 1, 2, 2, 2, 3, 3, 3, dotsize, 5 ] )
    pointx = x * dx - size
    pointy = y * dy - size
    if any(map(lambda p: p.contains(pointx, pointy), text_paths)):
        draw_text()