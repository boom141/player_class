import pygame,os

class asset_manager:
    IMAGE_DATABASE = {}

    def asset_init(self,entity):
        path = f'asset/{entity}'
        self.IMAGE_DATABASE[entity] = 'sample'
        temp_dict = {}
        for folder in os.listdir(path):
            temp = []
            for image in os.listdir(f'{path}/{folder}'):
                img = pygame.image.load(f'{path}/{folder}/{image}').convert_alpha()
                temp.append(img)
                temp_dict[folder] = temp

        self.IMAGE_DATABASE[entity] = temp_dict


