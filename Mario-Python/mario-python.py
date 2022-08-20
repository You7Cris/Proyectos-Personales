import arcade # modulo para crear el juego

SCREEN_WIDTH = 1000 # Ancho de la ventana
SCREEN_HEIGHT = 500 # Alto de la ventana
SCREEN_TITLE = "Mario"

#Constantes para escalar los sprites
CHARACTER_SCALING = 0.17
GROUND_SCALING = 0.20
CYLINDER_SCALING = 0.20

# Velocidad del jugador
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# Pixeles (mantener al minimo)
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

class MyGame(arcade.Window): # Permite crear la ventana en la pantalla

	def __init__(self):

		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) # Inicializar la superclase, se le pasan las constantes

		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE) # Se le da color

        # Listas que contendran los sprites
		self.coin_list = None
		self.wall_list = None
		self.player_list = None

		#Variable del sprite jugador
		self.player_sprite = None

		# Se utiliza para realizar un segumineto del desplazamiento
		self.view_bottom = 0
		
		self.view_left = 0

	def setup(self): # Funcion para los niveles
		self.player_list = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()
		self.coin_list = arcade.SpriteList()

		# Crea el jugador
		image_source = "mario.png"
		self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
		self.player_sprite.center_x = 64
		self.player_sprite.center_y = 93
		self.player_list.append(self.player_sprite)

		# Creacion del piso
        
        # Ese bucle es para colocar varios sprites horizontales
		for x in range(0, 1250, 64):
			wall = arcade.Sprite("ground.png", GROUND_SCALING)
			wall.center_x = x
			wall.center_y = 32
			self.wall_list.append(wall)

			# Muestra lista de coordenadas para colocar los sprites
		coordinate_list = [[512, 110],
							[256, 110],
							[768, 110]]

		for coordinate in coordinate_list:
			# Agregar un tubo al piso
			wall = arcade.Sprite("cylinder.png", CYLINDER_SCALING)
			wall.position = coordinate
			self.wall_list.append(wall)

		# Creacion del motor fisico
		self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)
	
	def on_draw(self):
		arcade.start_render()
		self.player_list.draw()
		self.wall_list.draw()

	def on_key_press(self, key, modifiers):
		# Se llama cada vez que se presiona la tecla

		if key == arcade.key.UP or key == arcade.key.W:
			if self.physics_engine.can_jump():
				self.player_sprite.change_y = PLAYER_JUMP_SPEED
		elif key == arcade.key.LEFT or key == arcade.key.A:
			self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
		elif key == arcade.key.RIGHT or key == arcade.key.D:
			self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

	def on_key_release(self, key, modifiers):
		# Se llama cuando el usuario suelta una clave

		if key == arcade.key.LEFT or key == arcade.key.A:
			self.player_sprite.change_x = 0
		elif key == arcade.key.RIGHT or key == arcade.key.D:
			self.player_sprite.change_x = 0

	def on_update(self, delta_time):
		# Logica de movimiento y juego

		# Mueve al jugador con el motor de fisica
		self.physics_engine.update()

		# --- Administrar desplazamiento ---

        # Seguimiento si necesitamos cambiar la ventana grafica
		changed = False

        # desplazarse a la izquierda
		left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
		if self.player_sprite.left < left_boundary:
			self.view_left -= left_boundary - self.player_sprite.left
			changed = True

		# desplazarse hacia la derecha
		right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
		if self.player_sprite.right > right_boundary:
			self.view_left += self.player_sprite.right - right_boundary
			changed = True

		# desplazarse hacia arriba
		top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
		if self.player_sprite.top > top_boundary:
			self.view_bottom += self.player_sprite.top - top_boundary
			changed = True

        # Desplazarse hacia abajo
		bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
		if self.player_sprite.bottom < bottom_boundary:
			self.view_bottom -= bottom_boundary - self.player_sprite.bottom
			changed = True

		if changed:
			# Solo desplazarse a numeros enteros. De lo conttrario, de lo contrario terminaremos con pixeles que no se alinean en la pantalla
			self.view_bottom = int(self.view_bottom)
			self.view_left = int(self.view_left)

			# Hacer el desplazamiento
			arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom,SCREEN_HEIGHT + self.view_bottom)

def main():
	window = MyGame()
	window.setup()
	arcade.run()

if __name__ == "__main__":
	main()
 
# Video del tutorial 
# https://www.youtube.com/watch?v=QpNExOWu3TA

# pip install arcade