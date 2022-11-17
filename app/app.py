import chess
from app.game_handler import GameHandler
from app.engine import Engine
from random import uniform

class App():
    def __init__(self):
        self.gui = None
        self.game = None
    
    def new_game(self, qt_game):
        current_settings = self.gui.qt_settings.get_current_settings()
        print(current_settings)
        engine_is_white = self.is_engine_white(current_settings)

        self.game = GameHandler(qt_game, Engine(engine_is_white, current_settings))
        qt_game.new_game(engine_is_white, current_settings['board_color'])
        if engine_is_white:
            self.game.run_engine()
    
    def new_analysis(self, qt_analysis):
        #TODO: engine_is_white: change based on pgn file
        current_settings = self.gui.qt_settings.get_current_settings()
        engine_is_white = self.is_engine_white(current_settings)
        qt_analysis.new_analysis(engine_is_white, current_settings['board_color'])

    def is_engine_white(self, current_settings):
        engine_is_white = None
        if current_settings['play_as'] == 1:
            engine_is_white = uniform(0, 1) > 0.5
        else:
            engine_is_white = current_settings['play_as'] == 3
        return engine_is_white
        