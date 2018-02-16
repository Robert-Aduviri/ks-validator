test = '''[Script Info]
Title: KS example file
ScriptType: v4.00+
WrapStyle: 0
PlayResX: 1080
PlayResY: 720
ScaledBorderAndShadow: yes
Video Aspect Ratio: 0
Video Zoom: 6
Video Position: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Start,Panton,72,&H00FFFFFF,&H000000FF,,,0,0,0,0,100,100,0,0,0,0,0,8,0,0,250,1
Style: End,Panton,60,&H00FFFFFF,&H000000FF,,,0,0,0,0,100,100,0,0,0,0,0,8,0,0,100,1
Style: Karaoke0,Panton,80,&H000000FF,&H00FFFFFF,,,0,0,0,0,100,100,0,0,0,0,0,8,0,0,250,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:04.00,Start,,0000,0000,0000,,N`KLABE
Dialogue: 0,0:00:00.00,0:00:04.00,Start,,0000,0000,0000,,AMOR DE UNA NOCHE
Dialogue: 0,0:00:00.00,0:00:04.00,Start,,0000,0000,0000,,TIEMPO 4:45
Dialogue: 0,0:00:20.00,0:00:20.13,Karaoke1,,0000,0000,300,,INSTRUMENTAL
Dialogue: 0,0:00:20.17,0:00:25.73,Karaoke0,,0000,0000,200,,{\kf303} {\kf23}ELLA {\kf10}ME {\kf44}ENTREGO
Dialogue: 0,0:00:20.30,0:00:26.47,Karaoke0,,0000,0000,300,,{\kf370} {\kf23}SU {\kf96}CUERPO
Dialogue: 0,0:00:20.47,0:00:28.17,Karaoke0,,0000,0000,400,,{\kf526} {\kf10}EN {\kf27}UNA {\kf33}NOCHE
Dialogue: 0,0:00:20.60,0:00:29.13,Karaoke0,,0000,0000,500,,{\kf597} {\kf90}CUALQUIERA
Dialogue: 0,0:00:26.43,0:00:30.43,Karaoke0,,0000,0000,100,,{\kf177} {\kf23}LUEGO {\kf60}ABANDONO
Dialogue: 0,0:00:26.83,0:00:33.33,Karaoke0,,0000,0000,200,,{\kf234} {\kf20}MI {\kf83}PUERTO
Dialogue: 0,0:00:28.90,0:00:34.30,Karaoke0,,0000,0000,300,,{\kf157} {\kf13}COMO {\kf13}UN {\kf67}BARCO {\kf30}DE {\kf103}VELA
Dialogue: 0,0:00:29.63,0:00:35.87,Karaoke0,,0000,0000,400,,{\kf374} {\kf23}ELLA {\kf17}ME {\kf46}DETUVO
Dialogue: 0,0:00:31.03,0:00:36.33,Karaoke0,,0000,0000,500,,{\kf334} {\kf13}EL {\kf83}ALMA
Dialogue: 0,0:00:33.83,0:00:38.40,Karaoke0,,0000,0000,100,,{\kf204} {\kf10}FUE {\kf13}UN {\kf23}RELOJ
Dialogue: 0,0:00:34.87,0:00:40.67,Karaoke0,,0000,0000,200,,{\kf150} {\kf23}SIN {\kf150}MANECILLAS
Dialogue: 0,0:00:36.87,0:00:41.07,Karaoke0,,0000,0000,300,,{\kf156} {\kf10}DE {\kf47}REPENTE {\kf43}ESTABA {\kf77}SOLO
Dialogue: 0,0:00:37.10,0:00:43.50,Karaoke0,,0000,0000,400,,{\kf357} {\kf33}CUANDO {\kf206}AMANECIA
Dialogue: 0,0:00:41.63,0:00:46.00,Karaoke0,,0000,0000,100,,{\kf190} {\kf24}TODO {\kf26}SE {\kf37}CAMBIO
Dialogue: 0,0:00:41.77,0:00:46.60,Karaoke0,,0000,0000,200,,{\kf270} {\kf20}ESA {\kf80}NOCHE
Dialogue: 0,0:00:44.20,0:00:48.67,Karaoke0,,0000,0000,300,,{\kf183} {\kf14}HASTA {\kf13}EL {\kf27}COLOR
Dialogue: 0,0:00:44.70,0:00:51.00,Karaoke0,,0000,0000,400,,{\kf190} {\kf17}DE {\kf16}LAS {\kf124}ESTRELLAS
Dialogue: 0,0:00:47.10,0:00:53.10,Karaoke0,,0000,0000,500,,{\kf167} {\kf20}TODO {\kf16}FUE {\kf34}TAN {\kf113}DIFERENTE
Dialogue: 0,0:00:47.20,0:00:57.50,Karaoke0,,0000,0000,100,,{\kf383} {\kf17}POR {\kf117}ELLA
Dialogue: 0,0:00:49.23,0:00:59.53,Karaoke0,,0000,0000,200,,{\kf394} {\kf20}POR {\kf20}QUE {\kf10}TE {\kf156}FUISTE
Dialogue: 0,0:00:51.67,0:01:02.53,Karaoke0,,0000,0000,300,,{\kf586} {\kf7}Y {\kf27}NO {\kf76}DEJASTE {\kf77}HUELLAS‘
Dialogue: 0,0:00:54.00,0:01:05.10,Karaoke0,,0000,0000,400,,{\kf553} {\kf10}ME {\kf47}VUELVO {\kf173}TRISTE
Dialogue: 0,0:00:58.10,0:01:10.33,Karaoke0,,0000,0000,500,,{\kf453} {\kf7}NO {\kf47}ENCUENTRO {\kf40}TU {\kf93}SILUETA
Dialogue: 0,0:01:00.33,0:01:12.90,Karaoke0,,0000,0000,100,,{\kf480} {\kf34}DESDE {\kf30}LA {\kf43}NOCHE {\kf193}AQUELLA
Dialogue: 0,0:01:03.30,0:01:13.83,Karaoke0,,0000,0000,200,,{\kf707} {\kf16}LUZ {\kf14}QUE {\kf13}SE {\kf143}DESAPARECE
Dialogue: 0,0:01:05.77,0:01:15.37,Karaoke0,,0000,0000,300,,{\kf713} {\kf30}AMOR {\kf17}QUE {\kf16}SE {\kf27}VA
Dialogue: 0,0:01:11.13,0:01:16.47,Karaoke0,,0000,0000,400,,{\kf274} {\kf3}Y {\kf17}NO {\kf83}VUELVE
Dialogue: 0,0:01:13.80,0:01:17.70,Karaoke0,,0000,0000,500,,{\kf167} {\kf30}PERO {\kf16}QUE {\kf14}ME {\kf30}SUBE
Dialogue: 0,0:01:14.47,0:01:20.63,Karaoke0,,0000,0000,100,,{\kf216} {\kf10}AL {\kf84}ALMA
Dialogue: 0,0:01:16.03,0:01:23.07,Karaoke0,,0000,0000,200,,{\kf170} {\kf24}COMO {\kf86}FUEGO {\kf40}QUE {\kf90}CRECE
Dialogue: 0,0:01:17.07,0:01:23.80,Karaoke0,,0000,0000,300,,{\kf360} {\kf3}Y {\kf17}YO {\kf13}TE {\kf40}SIGO {\kf117}SOÑANDO
Dialogue: 0,0:01:18.33,0:01:25.53,Karaoke0,,0000,0000,400,,{\kf480} {\kf60}PROCURANDO
Dialogue: 0,0:01:21.10,0:01:26.20,Karaoke0,,0000,0000,500,,{\kf270} {\kf10}QUE {\kf90}APAREZCA
Dialogue: 0,0:01:23.80,0:01:27.97,Karaoke0,,0000,0000,100,,{\kf180} {\kf23}ESE {\kf34}AMOR
Dialogue: 0,0:01:24.43,0:01:26.63,Karaoke0,,0000,0000,200,,{\kf184} {\kf10}QUE {\kf13}ME {\kf0}HACE {\kf0}FALTA
Dialogue: 0,0:01:26.00,0:01:30.77,Karaoke0,,0000,0000,300,,{\kf200} {\kf7}ESE {\kf50}AMOR
Dialogue: 0,0:01:26.70,0:01:28.67,Karaoke0,,0000,0000,400,,{\kf8670} {\kf0}QUE {\kf0}ME {\kf0}HACE {\kf0}FALTA
Dialogue: 0,0:01:26.87,0:01:31.63,Karaoke0,,0000,0000,500,,{\kf183} {\kf17}QUE {\kf13}ME {\kf107}ALIMENTA
Dialogue: 0,0:01:28.47,0:01:33.17,Karaoke0,,0000,0000,300,,{\kf233} {\kf23}TODO {\kf24}SE {\kf36}CAMBIO
Dialogue: 0,0:01:29.30,0:01:33.83,Karaoke0,,0000,0000,100,,{\kf240} {\kf20}ESA {\kf90}NOCHE
Dialogue: 0,0:01:31.20,0:01:35.87,Karaoke0,,0000,0000,200,,{\kf200} {\kf17}HASTA {\kf16}EL {\kf27}COLOR
Dialogue: 0,0:01:32.27,0:01:38.27,Karaoke0,,0000,0000,300,,{\kf156} {\kf10}DE {\kf24}LAS {\kf133}ESTRELLAS
Dialogue: 0,0:01:34.27,0:01:40.37,Karaoke0,,0000,0000,400,,{\kf163} {\kf23}TODO {\kf24}FUE {\kf30}TAN {\kf106}DIFERENTE
Dialogue: 0,0:01:34.37,0:01:44.73,Karaoke0,,0000,0000,500,,{\kf393} {\kf17}POR {\kf86}ELLA
Dialogue: 0,0:01:36.53,0:01:46.73,Karaoke0,,0000,0000,100,,{\kf387} {\kf17}POR {\kf23}QUE {\kf13}TE {\kf150}FUISTE
Dialogue: 0,0:01:38.83,0:01:49.77,Karaoke0,,0000,0000,200,,{\kf594} {\kf6}Y {\kf30}NO {\kf74}DEJASTE {\kf80}HUELLAS
Dialogue: 0,0:01:41.23,0:01:52.03,Karaoke0,,0000,0000,300,,{\kf554} {\kf3}ME {\kf53}VUELVO {\kf140}TRISTE
Dialogue: 0,0:01:45.30,0:01:53.43,Karaoke0,,0000,0000,400,,{\kf450} {\kf10}NO {\kf53}ENCUENTRO {\kf30}TU {\kf117}SILUETA
Dialogue: 0,0:01:47.47,0:01:54.67,Karaoke0,,0000,0000,500,,{\kf463} {\kf7}ES {\kf16}COMO {\kf20}UN {\kf80}SUEÑO
Dialogue: 0,0:01:50.63,0:02:02.70,Karaoke0,,0000,0000,100,,{\kf284} {\kf13}DEL {\kf20}QUE {\kf33}NO {\kf47}QUIERO
Dialogue: 0,0:01:52.53,0:02:02.70,Karaoke0,,0000,0000,200,,{\kf234} {\kf170}ESCAPAR
Dialogue: 0,0:01:54.33,0:02:02.70,Karaoke0,,0000,0000,300,,{\kf250} {\kf4}Y {\kf23}ES {\kf27}QUE {\kf16}TU {\kf87}IMAGEN
Dialogue: 0,0:01:55.33,0:02:02.70,Karaoke0,,0000,0000,400,,{\kf320} {\kf10}NO {\kf24}SE {\kf63}PUEDA {\kf233}REVELAR
Dialogue: 0,0:02:03.07,0:02:12.37,Karaoke0,,0000,0000,300,,{\kf136} {\kf587}INSTRUMENTAL
Dialogue: 0,0:02:12.60,0:02:16.27,Karaoke0,,0000,0000,50,,{\kf47} {\kf273}CORO
Dialogue: 0,0:02:16.63,0:02:25.17,Karaoke0,,0000,00000,100,{\kf124} {\kf33}TODO {\kf27}SE {\kf33}CAMBIO
Dialogue: 0,0:02:16.83,0:02:25.17,Karaoke0,,0000,0000,200,,{\kf204} {\kf26}ESA {\kf44}NOCHE {\kf40}PARA {\kf63}MI
Dialogue: 0,0:02:17.07,0:02:25.17,Karaoke0,,0000,0000,300,,{\kf400} {\kf6}Y {\kf14}HOY {\kf80}SOLO {\kf23}QUEDA
Dialogue: 0,0:02:17.17,0:02:25.17,Karaoke0,,0000,0000,400,,{\kf523} {\kf90}TRISTEZA
Dialogue: 0,0:02:25.43,0:02:35.63,Karaoke0,,0000,0000,100,,{\kf210} {\kf64}PORQUE
Dialogue: 0,0:02:25.63,0:02:35.63,Karaoke0,,0000,0000,200,,{\kf260} {\kf14}YO {\kf13}NO {\kf17}SE {\kf23}LO {\kf17}QUE {\kf13}ES
Dialogue: 0,0:02:25.80,0:02:35.63,Karaoke0,,0000,0000,300,,{\kf343} {\kf30}VIVIR {\kf30}SIN {\kf74}ELLA
Dialogue: 0,0:02:25.97,0:02:35.63,Karaoke0,,0000,0000,400,,{\kf530} {\kf33}VIVIR {\kf30}SIN {\kf70}ELLA
Dialogue: 0,0:02:36.03,0:02:45.83,Karaoke0,,0000,0000,100,,{\kf170} {\kf30}SE {\kf110}PERDIO‘EL {\kf64}COLOR
Dialogue: 0,0:02:36.27,0:02:45.83,Karaoke0,,0000,0000,200,,{\kf363} {\kf13}QUE {\kf17}MI {\kf40}ALMA {\kf67}ILUMINO
Dialogue: 0,0:02:36.40,0:02:45.83,Karaoke0,,0000,0000,300,,{\kf540} {\kf10}Y {\kf53}BRILLABA
Dialogue: 0,0:02:36.60,0:02:45.83,Karaoke0,,0000,0000,400,,{\kf587} {\kf10}EN {\kf20}LAS {\kf120}ESTRELLAS
Dialogue: 0,0:02:46.17,0:02:54.80,Karaoke0,,0000,0000,100,,{\kf173} {\kf10}POR {\kf30}EL {\kf70}CAMINO
Dialogue: 0,0:02:46.37,0:02:54.80,Karaoke0,,0000,0000,200,,{\kf276} {\kf14}QUE {\kf23}ELLA {\kf20}SE {\kf33}FUE
Dialogue: 0,0:02:46.50,0:02:54.80,Karaoke0,,0000,0000,300,,{\kf363} {\kf14}YO {\kf16}LA {\kf77}BUSQUE
Dialogue: 0,0:02:46.73,0:02:54.80,Karaoke0,,0000,0000,400,,{\kf467} {\kf37}Y {\kf13}YO {\kf27}NO {\kf63}ENCONTRE
Dialogue: 0,0:02:46.87,0:02:54.80,Karaoke0,,0000,0000,500,,{\kf603} {\kf27}SUS {\kf110}HUELLAS
Dialogue: 0,0:02:55.17,0:03:14.10,Karaoke0,,0000,0000,300,,{\kf256} {\kf50}INSTRUMENTAL
Dialogue: 0,0:03:14.43,0:03:20.77,Karaoke0,,0000,0000,100,,{\kf157} {\kf27}TODO {\kf90}TERMINO
Dialogue: 0,0:03:14.73,0:03:25.50,Karaoke0,,0000,0000,200,,{\kf260} {\kf24}TODO {\kf16}SE {\kf47}ACABO {\kf23}Y {\kf74}CAMBIO
Dialogue: 0,0:03:15.00,0:03:27.40,Karaoke0,,0000,0000,300,,{\kf580} {\kf17}Y {\kf40}ME {\kf60}TOMO {\kf26}POR {\kf120}SORPRESA
Dialogue: 0,0:03:15.30,0:03:28.13,Karaoke0,,0000,0000,400,,{\kf1023} {\kf20}NO {\kf37}CREI {\kf27}QUE {\kf20}IBA {\kf10}A {\kf66}DOLER
Dialogue: 0,0:03:15.43,0:03:30.90,Karaoke0,,0000,0000,500,,{\kf1204} {\kf20}ESE {\kf36}AMOR
Dialogue: 0,0:03:26.37,0:03:31.87,Karaoke0,,0000,0000,100,,{\kf180} {\kf40}CUANDO {\kf23}SE {\kf87}FUERA
Dialogue: 0,0:03:27.93,0:03:32.87,Karaoke0,,0000,0000,200,,{\kf300} {\kf17}SE {\kf63}FUE
Dialogue: 0,0:03:28.90,0:03:36.37,Karaoke0,,0000,0000,300,,{\kf300} {\kf23}NO {\kf30}DIJO {\kf40}ADIOS
Dialogue: 0,0:03:31.43,0:03:37.90,Karaoke0,,0000,0000,400,,{\kf144} {\kf6}Y {\kf24}ESO {\kf30}ME {\kf33}DOLIO {\kf33}DE {\kf117}VERAS
Dialogue: 0,0:03:32.40,0:03:39.03,Karaoke0,,0000,0000,500,,{\kf397} {\kf20}Y {\kf76}CREEME
Dialogue: 0,0:03:33.37,0:03:41.20,Karaoke0,,0000,0000,200,,{\kf456} {\kf14}QUE {\kf13}YA {\kf17}NO {\kf56}ENCUENTRO
Dialogue: 0,0:03:36.77,0:03:42.83,Karaoke0,,0000,0000,300,,{\kf223} {\kf7}QUE {\kf60}HACER
Dialogue: 0,0:03:38.83,0:03:42.97,Karaoke0,,0000,0000,400,,{\kf240} {\kf4}Y {\kf50}AQUI {\kf13}YO {\kf70}ESPERO
Dialogue: 0,0:03:39.43,0:03:44.73,Karaoke0,,0000,0000,500,,{\kf330} {\kf20}QUE {\kf87}VUELVA
Dialogue: 0,0:03:43.47,0:03:47.30,Karaoke0,,0000,0000,100,,{\kf133} {\kf23}TODO {\kf24}SE {\kf33}CAMBIO
Dialogue: 0,0:03:43.60,0:03:47.87,Karaoke0,,0000,0000,200,,{\kf207} {\kf26}ESA {\kf80}NOCHE
Dialogue: 0,0:03:45.27,0:03:49.93,Karaoke0,,0000,0000,300,,{\kf206} {\kf14}HASTA {\kf13}EL {\kf23}COLOR
Dialogue: 0,0:03:45.87,0:03:52.33,Karaoke0,,0000,0000,400,,{\kf200} {\kf13}DE {\kf17}LAS {\kf160}ESTRELLAS
Dialogue: 0,0:03:48.37,0:03:54.77,Karaoke0,,0000,0000,500,,{\kf170} {\kf13}TODO {\kf20}FUE {\kf33}TAN {\kf117}DIFERENTE
Dialogue: 0,0:03:48.47,0:03:58.77,Karaoke0,,0000,0000,100,,{\kf390} {\kf13}POR {\kf100}ELLA
Dialogue: 0,0:03:50.53,0:04:00.80,Karaoke0,,0000,0000,200,,{\kf390} {\kf20}POR {\kf20}QUE {\kf14}TE {\kf143}FUISTE
Dialogue: 0,0:03:53.03,0:04:03.67,Karaoke0,,0000,0000,300,,{\kf574} {\kf6}Y {\kf30}NO {\kf77}DEJASTE {\kf83}HUELLAS
Dialogue: 0,0:03:55.27,0:04:06.30,Karaoke0,,0000,0000,400,,{\kf553} {\kf10}ME {\kf53}VUELVO {\kf147}TRISTE
Dialogue: 0,0:03:59.33,0:04:11.77,Karaoke0,,0000,0000,500,,{\kf444} {\kf10}NO {\kf50}ENCUENTRO {\kf46}TU {\kf97}SILUETA
Dialogue: 0,0:04:01.60,0:04:11.77,Karaoke0,,0000,0000,100,,{\kf473} {\kf37}DESDE {\kf30}LA {\kf37}NOCHE {\kf143}AQUELLA
Dialogue: 0,0:04:06.70,0:04:11.77,Karaoke0,,0000,0000,300,,{\kf24670} {\kf50}INSTRUMENTAL
Dialogue: 0,0:04:11.77,0:04:16.77,Karaoke0,,0000,0000,300,,{\kf5000}{\kf5000}www.tropicalzone.tv'''


print('"' + '",\n"'.join([line for line in test.split('\n')]) + '"')
