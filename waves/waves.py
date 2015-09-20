cornu = ximport("cornu")
colors = ximport("colors")

# Painting waves
palette_blue = [ colors.hex( "#020034", "dark blue" ), colors.hex( "#0A5CD6", "aqua blue" ), colors.hex( "#333", "milk white" ) ]
palette_red = [ colors.hex( "#ff8844", "dark blue" ), colors.hex( "#ff8888", "aqua blue" ), colors.hex( "#832", "milk white" ) ]


# Draw Wave
def draw_wave(path, palette) : 
	strokewidth( choice( [ random( 0.1, 10 ), random( 0.1, 10 ) ] ) )
	stroke(color_to_alpha(choice(palette), random(0.1, 0.8) ))
	cornu.drawpath( path, close = False, flat = False )
	
def color_to_alpha(clr, alpha):
	return colors.rgb(clr.r, clr.g, clr.b, a=alpha)
	
def random_path():
	return [
        (random(0.1, 1.0), random(0.1, 1.0))
 	    for x in xrange(8)
 	]

def random_wave(n=8):
	phase = random(0, 0.3)	
	#phase = 0
	return [
#        (1.0-(x*(1.0+phase)/n), 0.4 if x%2 == 0 else 0.6)
		(1.0-(x*(1.0+phase)/n), random(0.4, 0.6))
 	    for x in xrange(-1, n+2)
 	]
	

 
nofill()
#for x in xrange(3):
#	draw_wave(random_path(), palette_blue)

for x in xrange(8):
	wave = random_wave()
	print(wave)
	draw_wave(wave, palette_red)

