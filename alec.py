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
		raise 'WTF'
	r = .5*diameter
	t_r = .5*t_diameter
	c_x = centerpt[0]
	c_y = centerpt[1]
	c_z = centerpt[2]
	i_value = r - t_r
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
			
	print 'G00 %s %s' %(round(new_x, 4), round(c_y, 4))
	print 'G01 F10 %s' %(round(c_z, 4))
	while d_cut <= z_depth:
		print 'G17 G03 I%s Z-%s' %(round(i_value, 4), round(d_cut, 4))
		d_cut += d_initial
	print 'G17 G03 I%s' %(round(i_value, 4))
	print 'G00 Z%s' %(round(rapid_h, 4))
	
	
	
		
if __name__ == "__main__":
#	circle(diameter=, centerpt=[1.0000,y,z], t_diameter=, d_cut=, z_depth=, rapid_h=, inside=True, spiral=True, hole=True)
	
	
	
	
	
	
	
	
