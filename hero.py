class Hero:
    hp = 0
    power = 0
    name = ''
    word = ''

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if final_hp > enemy_final_hp:
            print(f'{self.name}赢了')
        elif final_hp < enemy_final_hp:
            print('敌人赢了')
        else:
            print('本局打平了')

    def speak_lines(self):
        print(f'{self.word}')
