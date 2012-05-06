import math
import time 

def Single(Input_Speed, Stall_Torque, Teeth_1, Teeth_2, Wheel_Diameter):
	
	"""
	 Input/Output speed is in rpm
	 Drive Speed is in FPS
	"""
	
	
	I_s = Input_Speed
	I_t = Stall_Torque
	T_1 = round(Teeth_1,4)
	T_2 = round(Teeth_2,4)
	Rd = T_2/T_1
	Wd = Wheel_Diameter
	Wr = Wd*.5
	
	Cof = 1.2
	n_W = 4
	W = 140
	Nf = (W/n_W)*4.44
	Nm = 4
	
	Os = I_s / Rd
	Ot = I_t * Rd
	Ws = ((Os/60)*(Wd*math.pi))/12
	Pf = (Ot*Nm)/Wr
	Tf = (Nf*Cof)*n_W
	
	
	
	
	
	
	
	print 'Output Speed %d' % Os
	print 'Stall Torque %d' % Ot
	print 'Drive Speed %f' % round(Ws,2)
	print 'Drive Speed ' + str(round(Ws,2))
	
	
	if Pf >= Tf:
	
		print 'limited' 
		print 'Pushing Force %f' % round(Tf, 2)
		
	else:
	
		print 'Pushing Force %f' % round(Pf, 2)
	
	
	
	
if __name__ == "__main__":
  Single(4500, 20, 30, 45, 4)
	
	
	
