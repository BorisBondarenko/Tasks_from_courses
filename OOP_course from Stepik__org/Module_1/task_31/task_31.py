class Video():

    def __init__(self):
        self.name = None

    def create(self, name):
        self.name = name

    def play(self):
        return f"воспроизведение видео {self.name}"


class YouTube():
    video_base = []

    @classmethod
    def add_video(cls, video):
        cls.video_base.append(video)

    @classmethod
    def play(cls, video_indx):
        return cls.video_base[video_indx -1].play()


v1 = Video()
v1.create('Python')

v2 = Video()
v2.create('Python ООП')

video_hosting = YouTube()
video_hosting.add_video(v1)
video_hosting.add_video(v2)

print(video_hosting.play(1))
print(video_hosting.play(2))