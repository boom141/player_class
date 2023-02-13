import pygame
from pygame.locals import*
from scripts.entity.animation import animation_manager

class entity_manager:
	def __init__(self, player_rect, player_offset):
		self.rect = player_rect
		self.offset = player_offset
		self.GRAVITY = .5
		self.SPEED = 5
		self.jump_height = 13
		self.momentum_Y = 0
		self.player_move = [0,0]

		self.facing = False
		self.jump_once = True
		self.is_falling = 0
		self.init_state = 'idle'
		self.animation_init = animation_manager()
		self.collision_types = {'top':False,'bottom':False,'right':False,'left':False} 


	def collision(self,tile_rects):
		hit_list = []
		for tile in tile_rects:
			if self.rect.colliderect(tile):
				hit_list.append(tile)

		return hit_list

	def handle_collision(self,tile_rects):
		self.collision_types = {'top':False,'bottom':False,'right':False,'left':False} 
		self.rect.x += self.player_move[0]
		hit_list = self.collision(tile_rects)
		for tile in hit_list:
			if self.player_move[0] > 0:
				self.rect.right = tile.left 
				self.collision_types['right'] = True
			elif self.player_move[0] < 0:
				self.rect.left = tile.right 
				self.collision_types['left'] = True
		self.rect.y += self.player_move[1]
		hit_list = self.collision(tile_rects)
		for tile in hit_list:
			if self.player_move[1] > 0:
				self.rect.bottom = tile.top
				self.collision_types['bottom'] = True
			elif self.player_move[1]  < 0:
				self.rect.top = tile.bottom
				self.collision_types['top'] = True
				
	def controller(self,delta_time,tile_rects):
		self.player_move = [0,0]
		if pygame.key.get_pressed()[K_d]:
			self.facing = False
			self.player_move[0] += self.SPEED * delta_time
		if pygame.key.get_pressed()[K_a]:
			self.facing = True
			self.player_move[0] -= self.SPEED * delta_time
		if pygame.key.get_pressed()[K_SPACE] and self.jump_once:
			self.momentum_Y = -self.jump_height
			self.jump_once = False

		self.player_move[1] += self.momentum_Y // 1.5
		self.momentum_Y += self.GRAVITY * delta_time
		if self.momentum_Y > self.jump_height:
			self.momentum_Y = self.jump_height
		
		self.handle_collision(tile_rects)
		if self.collision_types['bottom']:
			self.jump_once = True

	def entity_state(self):
		self.init_state = 'idle'
		if self.jump_once == False and self.momentum_Y < 0:
			self.init_state = 'jumping'
		elif self.jump_once == False and self.momentum_Y > 0:
			self.init_state = 'falling'
		elif self.player_move[0] > 0 or self.player_move[0] < 0 :
			self.init_state = 'running'
		