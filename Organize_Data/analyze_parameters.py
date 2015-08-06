
# Class that is meant to evaluate parameters and return a grade
# for two song data that are passed to it
class ParamMethods(object):

    def __init__(self, genre = 1, key = 1, bpm = 1):
        # we can override these later based on our research
        # these constructor variables must add up to a whole number
        # that is equal to how many they are
        self.genre_weight = genre
        self.key_weight = key
        self.bpm_weight = bpm

    # Returns a grade for a transition betweeen two songs
    def grade_parameters( self, first_song, second_song):
    # iterate through kwargs and give a grade based on each parameter, take the average
        grade = 0.0
        num_of_params = 0.0

        self.song_one = first_song
        self.song_two = second_song

        # compare two songs
        for (key, value) in first_song.iteritems():
            if key in second_song:
                value2 = second_song[key]
                # analyze the parameter
                param_func_grade = self._assign_function(key) # which parameter to analyze?
                grade += param_func_grade() # grade the overlap, of two things, such as bpm
            else:
                print "%s ; inconsistent keys received\n" % (key)
            num_of_params += 1

        return (grade/num_of_params) # return the average

    # assign a function to grade two parameters based on the name of the dict key
    # this is meant to allow us to change the parameters that we use flexibly
    def _assign_function(self, key_from_dict):
        if key_from_dict in 'notes':
            return self._grade_notes
        elif key_from_dict in 'key':
            return self._grade_key
        elif key_from_dict in 'bpm':
            return self._grade_bpm
        else:
            return self._zero_func

    def _grade_notes(self):
        return 1
    def _grade_key(self):
        return 1
    def _grade_bpm(self):
        return 1
    def _zero_func(self):
        return 0
