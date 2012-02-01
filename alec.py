import sys, math



def circle(diameter, centerpt, t_diameter, d_cut, z_depth, rapid_h, inside=True, spiral=True, hole=True):
	"""
	Radius should be a float
	Center point should be a list of three floats [1.0, 1.0, 1.0]
	If not inside, Outside
	If not spiral, plunge
	If not hole, pocket
	"""
	if (not hole) and (not inside):
		print 'WTF'
	r = .5*diameter
	t_r = .5*t_diameter
	c_x = centerpt[0]
	c_y = centerpt[1]
	c_z = centerpt[2]
	if inside:
		i_value = r - t_r
	else:
		i_value = r + t_r
	d_initial = d_cut
	if inside and hole:
		new_x = c_x - r + t_r
	if (not inside) and hole:
		new_x = c_x - r - t_r
	"""
	if inside and (not hole):
		new_x = c_x - t_r
			print 'G00 %s %s' %(new_x, c_y)
			print 'G01 F10 %s' %(c_z)
			while d_cut =< z_depth:
				print 'G17 G03 I%s Z-%s' %(i_value, d_cut)
				d_cut += d_initial
			print 'G17 G03 I%s' %(i_value)
			print 'G00 Z%s' %(rapid_h)
	"""		
			
	print 'G00 X%s Y%s' %(round(new_x, 4), round(c_y, 4))
	print 'G01 F10 %s' %(round(c_z, 4))
	while d_cut <= z_depth:
		print 'G17 G03 I%s Z-%s' %(round(i_value, 4), round(d_cut, 4))
		d_cut += d_initial
	print 'G17 G03 I%s' %(round(i_value, 4))
	print 'G00 Z%s' %(round(rapid_h, 4))
	
	
	
		
if __name__ == "__main__":
	while True:
		diameter=input('Diameter of circle=')
		cp_x = input('Centerpoint, x-coord: =')
		cp_y = input('Centerpoint, y-coord: =')
		cp_z = input('Centerpoint, z-coord: =')
		cp = [cp_x, cp_y, cp_z]
		t_diameter = input('Tool diameter=')
		d_cut = input('d_cut=')
		z_depth = input('z_depth=')
		rapid_h = input('rapid_h=')
		in_ans = raw_input('Inside or Outside? [I/o] ')
		inside = in_ans.lower() != 'o'
		sp_ans = raw_input('Spiral or Plunge? [S/p] ')
		spiral = sp_ans.lower() != 'p'
		hole_ans = raw_input('Hole or Pocket? [H/p] ')
		hole = hole_ans.lower() != 'p'
		circle(diameter=diameter, centerpt=cp, t_diameter=t_diameter, d_cut=d_cut, z_depth=z_depth, rapid_h=rapid_h, inside=inside, spiral=spiral, hole=hole)
	
	
	
	
	
	
	
	
