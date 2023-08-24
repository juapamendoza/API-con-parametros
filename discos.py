from fastapi import FastAPI

#pydantic va a obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

# crear el objeto a partir de la clase
discosApp = FastAPI()

#definir la entidad Disco con sus atributos y su tipo de datos
class Disco(BaseModel):
    id:int
    nombre:str
    artista:str
    genero:str

discos_list=[Disco(id=1, nombre="Midnights", artista="Taylor Swift", genero="Pop"),
            Disco(id=2, nombre="reputation", artista="Taylor Swift", genero="Pop"),
            Disco(id=3, nombre="Lover", artista="Taylor Swift", genero="Pop"),
            Disco(id=4, nombre="1989", artista="Taylor Swift", genero="Pop"),
            Disco(id=5, nombre="Taylor Swift", artista="Taylor Swift", genero="Country"),
            Disco(id=6, nombre="Fearless", artista="Taylor Swift", genero="Country"),
            Disco(id=7, nombre="Speak Now", artista="Taylor Swift", genero="Country"),
            Disco(id=8, nombre="Red", artista="Taylor Swift", genero="Pop"),
            Disco(id=9, nombre="folklore", artista="Taylor Swift", genero="Indie"),
            Disco(id=10, nombre="evermore", artista="Taylor Swift", genero="Indie"),
            Disco(id=11, nombre="Did you know that there's a tunnel under Ocean Blvd", artista="Lana del Rey", genero="Alternative"),
            Disco(id=12, nombre="Blue Banisters", artista="Lana del Rey", genero="Alternative"),
            Disco(id=13, nombre="Chemtrails Over The Country Club", artista="Lana del Rey", genero="Alternative"),
            Disco(id=14, nombre="Norman Fucking Rockwell", artista="Lana del Rey", genero="Alternative"),
            Disco(id=15, nombre="Lust For Life", artista="Lana del Rey", genero="Alternative"),
            Disco(id=16, nombre="Honeymoon", artista="Lana del Rey", genero="Alternative"),
            Disco(id=17, nombre="Ultraviolence", artista="Lana del Rey", genero="Alternative"),
            Disco(id=18, nombre="Born to Die", artista="Lana del Rey", genero="Alternative"),
            Disco(id=19, nombre="Paradise", artista="Lana del Rey", genero="Alternative"),
            Disco(id=20, nombre="Pure Heroine", artista="Lorde", genero="Alternative"),
            Disco(id=21, nombre="The Love Club", artista="Lorde", genero="Alternative"),
            Disco(id=22, nombre="Melodrama", artista="Lorde", genero="Pop"),
            Disco(id=23, nombre="Solar Power", artista="Lorde", genero="Alternative"),
            Disco(id=24, nombre="Bubblebath", artista="Poppy", genero="Pop"),
            Disco(id=25, nombre="Poppy.Computer", artista="Poppy", genero="Pop"),
            Disco(id=26, nombre="Am I a Girl?", artista="Poppy", genero="Pop"),
            Disco(id=27, nombre="Choke", artista="Poppy", genero="Experimental"),
            Disco(id=28, nombre="I Disagree", artista="Poppy", genero="Rock"),
            Disco(id=29, nombre="A Very Poppy Christmas", artista="Poppy", genero="Rock"),
            Disco(id=30, nombre="EAT (NXT Soundtrack)", artista="Poppy", genero="Rock"),
            Disco(id=31, nombre="Flux", artista="Poppy", genero="Rock"),
            Disco(id=32, nombre="Stagger", artista="Poppy", genero="Rock"),
            Disco(id=33, nombre="Knockoff", artista="Poppy", genero="Rock"),
            Disco(id=34, nombre="World War Joy", artista="The Chainsmokers", genero="Pop"),
            Disco(id=35, nombre="So Far So Good", artista="The Chainsmokers", genero="Pop"),
            Disco(id=36, nombre="Bouquet", artista="The Chainsmokers", genero="Pop"),
            Disco(id=37, nombre="Collage", artista="The Chainsmokers", genero="Pop"),
            Disco(id=38, nombre="Memories...Do Not Open", artista="The Chainsmokers", genero="Pop"),
            Disco(id=39, nombre="Sick Boy", artista="The Chainsmokers", genero="Pop"),
            Disco(id=40, nombre="Los Angeles", artista="ROSALIA", genero="Indie"),
            Disco(id=41, nombre="El Mal Querer", artista="ROSALIA", genero="Alternative"),
            Disco(id=42, nombre="MOTOMAMI", artista="ROSALIA", genero="Pop"),
            Disco(id=43, nombre="MTV Unplugged", artista="Katy Perry", genero="Pop"),
            Disco(id=44, nombre="One Of The Boys", artista="Katy Perry", genero="Pop"),
            Disco(id=45, nombre="Teenage Dreams", artista="Katy Perry", genero="Pop"),
            Disco(id=46, nombre="PRISM", artista="Katy Perry", genero="Pop"),
            Disco(id=47, nombre="Witness", artista="Katy Perry", genero="Pop"),
            Disco(id=48, nombre="Smile", artista="Katy Perry", genero="Pop"),
            Disco(id=49, nombre="Glass Animals", artista="Glass Animals", genero="Indie"),
            Disco(id=50, nombre="ZABA", artista="Glass Animals", genero="Indie"),
            Disco(id=51, nombre="How To Be A Human Being", artista="Glass Animals", genero="Indie"),
            Disco(id=52, nombre="Dreamland", artista="Glass Animals", genero="Pop"),
            Disco(id=53, nombre="I Don't Wanna Grow Up", artista="Bebe Rexha", genero="Pop"),
            Disco(id=54, nombre="All Your Fault Pt. 1", artista="Bebe Rexha", genero="Pop"),
            Disco(id=55, nombre="All Your Fault Pt. 2", artista="Bebe Rexha", genero="Pop"),
            Disco(id=56, nombre="Expectations", artista="Bebe Rexha", genero="Pop"),
            Disco(id=57, nombre="Better Mistakes", artista="Bebe Rexha", genero="Pop"),
            Disco(id=58, nombre="Bebe", artista="Bebe Rexha", genero="Pop"),
            Disco(id=59, nombre="For You", artista="Selena Gomez", genero="Pop"),
            Disco(id=60, nombre="Kiss & Tell", artista="Selena Gomez", genero="Pop"),
            Disco(id=61, nombre="A Year Without Rain", artista="Selena Gomez", genero="Pop"),
            Disco(id=62, nombre="When the Sun Goes Down", artista="Selena Gomez", genero="Pop"),
            Disco(id=63, nombre="Stars Dance", artista="Selena Gomez", genero="Pop"),
            Disco(id=64, nombre="Revival", artista="Selena Gomez", genero="Pop"),
            Disco(id=65, nombre="Rare", artista="Selena Gomez", genero="Pop"),
            Disco(id=66, nombre="Revelacion", artista="Selena Gomez", genero="Latin"),
            Disco(id=67, nombre="Whatever People Say I Am, That's What I Am Not", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=68, nombre="Who The Fuck Are Arctic Monkeys?", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=69, nombre="Brainstorm", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=70, nombre="Favourite Worst Nightmare", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=71, nombre="Fluorescent Adolescent", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=72, nombre="Teddy Picker", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=73, nombre="Humbug", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=74, nombre="Cornerstone", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=75, nombre="My Propeller", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=76, nombre="Suck It and See", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=77, nombre="AM", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=78, nombre="Tranquility Base Hotel & Casino", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=79, nombre="The Car", artista="Arctic Monkeys", genero="Indie"),
            Disco(id=80, nombre="Aprendiendo a Aprender", artista="Carla Morrison", genero="Alternative"),
            Disco(id=81, nombre="Mientras Tu Dormias", artista="Carla Morrison", genero="Alternative"),
            Disco(id=82, nombre="Dejenme Llorar", artista="Carla Morrison", genero="Alternative"),
            Disco(id=83, nombre="Jugando en Serio", artista="Carla Morrison", genero="Alternative"),
            Disco(id=84, nombre="Amor Supremo", artista="Carla Morrison", genero="Alternative"),
            Disco(id=85, nombre="El Renacimiento", artista="Carla Morrison", genero="Alternative"),
            Disco(id=86, nombre="The Slow Rush", artista="Tame Impala", genero="Alternative"),
            Disco(id=87, nombre="Currents", artista="Tame Impala", genero="Alternative"),
            Disco(id=88, nombre="Lonerism", artista="Tame Impala", genero="Alternative"),
            Disco(id=89, nombre="InnerSpeaker", artista="Tame Impala", genero="Alternative"),
            Disco(id=90, nombre="Sentio", artista="Martin Garrix", genero="Electronic"),
            Disco(id=91, nombre="Martin Garrix Presents STMPD RCRDS, Vol. 001", artista="Martin Garrix", genero="Electronic"),
            Disco(id=92, nombre="2019 Remixed", artista="Martin Garrix", genero="Electronic"),
            Disco(id=93, nombre="Gold Skies", artista="Martin Garrix", genero="Electronic"),
            Disco(id=94, nombre="Seven", artista="Martin Garrix", genero="Electronic"),
            Disco(id=95, nombre="Joytime", artista="Marshmello", genero="Electronic"),
            Disco(id=96, nombre="Joytime II", artista="Marshmello", genero="Electronic"),
            Disco(id=97, nombre="Joytime III", artista="Marshmello", genero="Electronic"),
            Disco(id=98, nombre="Shockwave", artista="Marshmello", genero="Electronic"),
            Disco(id=99, nombre="Mellokillaz", artista="Marshmello", genero="Electronic"),
            Disco(id=100, nombre="With Hearts As One", artista="Hillsong United", genero="Christian"),
            Disco(id=101, nombre="Of Dirt And Grace", artista="Hillsong United", genero="Christian"),
            Disco(id=102, nombre="The White Album", artista="Hillsong United", genero="Christian"),
            Disco(id=103, nombre="Everyday (Live)", artista="Hillsong United", genero="Christian"),
            Disco(id=104, nombre="Best Friend: United Live", artista="Hillsong United", genero="Christian"),
            Disco(id=105, nombre="King of Magesty", artista="Hillsong United", genero="Christian"),
            Disco(id=106, nombre="To The Ends Of The Earth", artista="Hillsong United", genero="Christian"),
            Disco(id=107, nombre="More Than Life (Live)", artista="Hillsong United", genero="Christian"),
            Disco(id=108, nombre="Look To You", artista="Hillsong United", genero="Christian"),
            Disco(id=109, nombre="United We Stand", artista="Hillsong United", genero="Christian"),
            Disco(id=110, nombre="Across The Earth: Tear Down The Walls", artista="Hillsong United", genero="Christian"),
            Disco(id=111, nombre="Live In Miami", artista="Hillsong United", genero="Christian"),
            Disco(id=112, nombre="People (Live)", artista="Hillsong United", genero="Christian"),
            Disco(id=113, nombre="All Of The Above", artista="Hillsong United", genero="Christian"),
            Disco(id=114, nombre="Aftermath", artista="Hillsong United", genero="Christian"),
            Disco(id=115, nombre="Zion", artista="Hillsong United", genero="Christian"),
            Disco(id=116, nombre="Empires", artista="Hillsong United", genero="Christian"),
            Disco(id=117, nombre="Wonder", artista="Hillsong United", genero="Christian"),
            Disco(id=118, nombre="(in the meantime)", artista="Hillsong United", genero="Christian"),
            Disco(id=119, nombre="(in the meantime) Vol. II", artista="Hillsong United", genero="Christian"),
            Disco(id=120, nombre="Are We There Yet?", artista="Hillsong United", genero="Christian"),
            Disco(id=121, nombre="LAS QUE NO IBAN A SALIR", artista="Bad Bunny", genero="Latin"),
            Disco(id=122, nombre="X 100PRE", artista="Bad Bunny", genero="Latin"),
            Disco(id=123, nombre="OASIS", artista="Bad Bunny", genero="Latin"),
            Disco(id=124, nombre="YHLQMDLG", artista="Bad Bunny", genero="Latin"),
            Disco(id=125, nombre="EL ULTIMO TOUR DEL MUNDO", artista="Bad Bunny", genero="Latin"),
            Disco(id=126, nombre="Un Verano Sin Ti", artista="Bad Bunny", genero="Latin"),
            Disco(id=127, nombre="Todo Es Diferente", artista="Natanael Cano", genero="Latin"),
            Disco(id=128, nombre="Corridos Tumbados", artista="Natanael Cano", genero="Latin"),
            Disco(id=129, nombre="Trap Tumbado", artista="Natanael Cano", genero="Latin"),
            Disco(id=130, nombre="Soy El Nata", artista="Natanael Cano", genero="Latin"),
            Disco(id=131, nombre="Las 3 Torres", artista="Natanael Cano", genero="Latin"),
            Disco(id=132, nombre="Mi Nuevo Yo", artista="Natanael Cano", genero="Latin"),
            Disco(id=133, nombre="Nata", artista="Natanael Cano", genero="Latin"),
            Disco(id=134, nombre="A Mis 20", artista="Natanael Cano", genero="Latin"),
            Disco(id=135, nombre="NataKong", artista="Natanael Cano", genero="Latin"),
            Disco(id=136, nombre="Nata Montana", artista="Natanael Cano", genero="Latin"),
            Disco(id=137, nombre="MAÑANA SERA BONITO", artista="Karol G", genero="Latin"),
            Disco(id=138, nombre="KG0516", artista="Karol G", genero="Latin"),
            Disco(id=139, nombre="OCEAN", artista="Karol G", genero="Latin"),
            Disco(id=140, nombre="Unstoppable", artista="Karol G", genero="Latin"),
            Disco(id=141, nombre="72 Seasons", artista="Metallica", genero="Metal"),
            Disco(id=142, nombre="Metallica Live At Woodstck '94", artista="Metallica", genero="Metal"),
            Disco(id=143, nombre="The Metallica Blacklist", artista="Metallica", genero="Metal"),
            Disco(id=144, nombre="Hardwired...To Self-Destruct", artista="Metallica", genero="Metal"),
            Disco(id=145, nombre="Death Magnetic", artista="Metallica", genero="Metal"),
            Disco(id=146, nombre="St. Anger", artista="Metallica", genero="Metal"),
            Disco(id=147, nombre="Reload", artista="Metallica", genero="Metal"),
            Disco(id=148, nombre="Load", artista="Metallica", genero="Metal"),
            Disco(id=149, nombre="Remaining Memories: The Interview", artista="Metallica", genero="Metal"),
            Disco(id=150, nombre="Live S**t: Binge & Purge", artista="Metallica", genero="Metal"),
            Disco(id=151, nombre="Metallica", artista="Metallica", genero="Metal"),
            Disco(id=152, nombre="...And Justice For All", artista="Metallica", genero="Metal"),
            Disco(id=153, nombre="Master of Puppets", artista="Metallica", genero="Metal"),
            Disco(id=154, nombre="Ride The Lightning", artista="Metallica", genero="Metal"),
            Disco(id=155, nombre="UTOPIA", artista="Travis Scott", genero="Hip-Hop"),
            Disco(id=156, nombre="ASTROWORLD", artista="Travis Scott", genero="Hip-Hop"),
            Disco(id=157, nombre="Huncho Jack, Jack Huncho", artista="Travis Scott", genero="Hip-Hop"),
            Disco(id=158, nombre="Birds in the Trap Sing McKnight", artista="Travis Scott", genero="Hip-Hop"),
            Disco(id=159, nombre="Rodeo (Expanded Edition)", artista="Travis Scott", genero="Hip-Hop"),
            Disco(id=160, nombre="JACKBOYS", artista="Travis Scott", genero="Hip-Hop"),
            Disco(id=161, nombre="Her Loss", artista="Drake", genero="Hip-Hop"),
            Disco(id=162, nombre="Honestly, Nevermind", artista="Drake", genero="Hip-Hop"),
            Disco(id=163, nombre="Certified Lover Boy", artista="Drake", genero="Hip-Hop"),
            Disco(id=164, nombre="Scorpion", artista="Drake", genero="Hip-Hop"),
            Disco(id=165, nombre="More Life", artista="Drake", genero="Hip-Hop"),
            Disco(id=166, nombre="Views", artista="Drake", genero="Hip-Hop"),
            Disco(id=167, nombre="If You're Reading This It's Too Late", artista="Drake", genero="Hip-Hop"),
            Disco(id=168, nombre="Nothing Was The Same", artista="Drake", genero="Hip-Hop"),
            Disco(id=169, nombre="Take Care (Deluxe)", artista="Drake", genero="Hip-Hop"),
            Disco(id=170, nombre="Thank Me Later", artista="Drake", genero="Hip-Hop"),
            Disco(id=171, nombre="Dark Lane Demo Tapes", artista="Drake", genero="Hip-Hop"),
            Disco(id=172, nombre="Care Package", artista="Drake", genero="Hip-Hop"),
            Disco(id=173, nombre="What a Time To Be Alive", artista="Drake", genero="Hip-Hop"),
            Disco(id=174, nombre="So Far Gone", artista="Drake", genero="Hip-Hop"),
            Disco(id=175, nombre="Tarzan (Banda Sonora Original)", artista="Various Artists", genero="Soundtrack"),
            Disco(id=176, nombre="UNDERTALE Soundtrack", artista="Various Artists", genero="Soundtrack"),
            Disco(id=177, nombre="Sing 2 (Original Motion Picture Soundtrack)", artista="Various Artists", genero="Soundtrack"),
            Disco(id=178, nombre="A Star Is Born Soundtrack", artista="Lady Gaga", genero="Soundtrack"),
            Disco(id=179, nombre="Euphoria (Original Score from the HBO Series)", artista="Labirinth", genero="Soundtrack"),
            Disco(id=180, nombre="Love For Sale (Deluxe)", artista="Lady Gaga", genero="Jazz"),
            Disco(id=181, nombre="Chromatica", artista="Lady Gaga", genero="Pop"),
            Disco(id=182, nombre="Joanne", artista="Lady Gaga", genero="Indie"),
            Disco(id=183, nombre="Cheek to Cheek", artista="Lady Gaga", genero="Jazz"),
            Disco(id=184, nombre="ARTPOP", artista="Lady Gaga", genero="Pop"),
            Disco(id=185, nombre="Born this Way", artista="Lady Gaga", genero="Pop"),
            Disco(id=186, nombre="The Fame Monster", artista="Lady Gaga", genero="Pop"),
            Disco(id=187, nombre="The Fame", artista="Lady Gaga", genero="Pop"),
            Disco(id=188, nombre="Like a Prayer", artista="Madonna", genero="Pop"),
            Disco(id=189, nombre="La La Land (Original Motion Picture Soundtrack)", artista="Various Artists", genero="Soundtrack"),
            Disco(id=190, nombre="Mexico And Mariachis", artista="Various Artists", genero="Soundtrack"),
            Disco(id=191, nombre="Minecraft - Volume Alpha", artista="C418", genero="Soundtrack"),
            Disco(id=192, nombre="Sonic Frontiers Original Soundtrack", artista="SEGA", genero="Soundtrack"),
            Disco(id=193, nombre="Mamma Mia! The Movie Soundtrack", artista="Various Artists", genero="Soundtrack"),
            Disco(id=194, nombre="Up (Original Motion Picture Soundtrack)", artista="Various Artists", genero="Soundtrack"),
            Disco(id=195, nombre="Elemental (Original Motion Picture Soundtrack)", artista="Various Artists", genero="Soundtrack"),
            Disco(id=196, nombre="Beam Me Up Scotty", artista="Nicki Minaj", genero="Hip-Hop"),
            Disco(id=197, nombre="Queen", artista="Nicki Minaj", genero="Hip-Hop"),
            Disco(id=198, nombre="The Pinkprint", artista="Nicki Minaj", genero="Hip-Hop"),
            Disco(id=199, nombre="Pink Friday...Roman Reloaded", artista="Nicki Minaj", genero="Hip-Hop"),
            Disco(id=200, nombre="Queen Radio: Volume 1", artista="Nicki Minaj", genero="Hip-Hop")]
            
@discosApp.get("/discosclass")
async def discos():
    return (discos_list)

@discosApp.get("/discosclass/{id}")
async def discosclass(id:int):
    discoID=filter(lambda disco: disco.id == id, discos_list)
    try:
        return list(discoID)[0]
    except:
        return{"error": "No se ha encontrado el disco"} 
    
# uvicorn [nombre_archivo]:[nombre_objeto] --reload