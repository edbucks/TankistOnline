import pyglet

class Tank:

	sprTank = None
	sprExplosion = None
	
	explosion = None
	explosionIndex = None
	
	rotation = 0
	realRotation = 0
	
	x = 0
	y = 0
	
	absx = 0 #Absolute xy values.
	absy = 0
	
	def loadImage(self, pathToImage, imageName):
		
		#Initialize this tank sprite with an image.
		
		pyglet.resource.path = [pathToImage]
		pyglet.resource.reindex()
	
		imgImage = pyglet.resource.image(imageName)
		
		imgImage = self.centralize(imgImage)
		
		self.sprTank = pyglet.sprite.Sprite(img=imgImage, x=self.x, y=self.y)

	def setXY(self):
		
		self.sprTank.x = self.x
		self.sprTank.y = self.y
		self.sprExplosion.x = self.x
		self.sprExplosion.y = self.y

	def explode(self):
		
		#Trigger the explosion.

		self.explosion = True
		self.explosionIndex = 0
		
	def rotate(self):
		
		#Rotate both the tank and the explosion.
		
		self.sprTank.rotation = self.rotation
		self.sprExplosion.rotation = self.rotation

			
	def draw(self):
		
		#Draw the tank. If an explosion is present, explode that, too.
		
		self.sprTank.draw()
		
		if self.explosion:
		
			self.explosionIndex += 1
		
			if self.explosionIndex == 10:
		
				self.explosion = False
				self.explosionIndex = None
				
			else:
				
				self.sprExplosion.draw()
				
	def centralize(self, image):
		
		#Internal function to centralize an image before it is used in a sprite,
		#that it may rotate evenly upon its axis.
		
		image.anchor_x = image.width // 2
		image.anchor_y = image.height // 2
		
		return image
		
	def move(self):
		
		#Internal function to change the tank's x and y.
		
		self.sprTank.x = self.x
		self.sprTank.y = self.y
		self.sprExplosion.x = self.x
		self.sprExplosion.y = self.y
		
	def __init__(self):

		#We preload the explosion, as no tank shall go unscathed.
		
		pyglet.resource.path = ['gfx/sprites']
		pyglet.resource.reindex()
		
		imgExplode = pyglet.resource.image("explode.png")
		imgExplode = self.centralize(imgExplode)
		
		self.sprExplosion = pyglet.sprite.Sprite(img=imgExplode, x=self.x, y=self.y)
		
		imgExplode = None
