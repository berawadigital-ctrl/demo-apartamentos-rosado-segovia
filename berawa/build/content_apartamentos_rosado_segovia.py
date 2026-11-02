# Contenido de la demo Apartamentos Rosado (Segovia) (es/en/fr/de). Hechos de apartamentosrosado.es leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Huella Romana y Luz de Segovia','Mirador de San Lorenzo y Valle del Eresma'],'en':['Huella Romana and Luz de Segovia','Mirador de San Lorenzo and Valle del Eresma'],'fr':['Huella Romana et Luz de Segovia','Mirador de San Lorenzo et Valle del Eresma'],'de':['Huella Romana und Luz de Segovia','Mirador de San Lorenzo und Valle del Eresma']}
RD={
'es':['Lofts de 33 m² para 2 a 4 personas, luminosos e insonorizados, con cama de matrimonio, sofá cama, cocina completa y baño con ducha.','Lofts de 36 m² para 2 a 4 personas, con amplias ventanas, cama king size, sofá cama, cocina totalmente equipada y Smart TV.'],
'en':['33 m² lofts for 2 to 4 people, bright and soundproofed, with a double bed, sofa bed, full kitchen and bathroom with shower.','36 m² lofts for 2 to 4 people, with large windows, king-size bed, sofa bed, fully equipped kitchen and Smart TV.'],
'fr':['Lofts de 33 m² pour 2 à 4 personnes, lumineux et insonorisés, avec lit double, canapé-lit, cuisine complète et salle de bains avec douche.','Lofts de 36 m² pour 2 à 4 personnes, avec grandes fenêtres, lit king size, canapé-lit, cuisine entièrement équipée et Smart TV.'],
'de':['Lofts mit 33 m² für 2 bis 4 Personen, hell und schallisoliert, mit Doppelbett, Schlafsofa, voll ausgestatteter Küche und Bad mit Dusche.','Lofts mit 36 m² für 2 bis 4 Personen, mit großen Fenstern, Kingsize-Bett, Schlafsofa, voll ausgestatteter Küche und Smart-TV.']}
ART={
'hero':('arches',6611,['#2a2320','#b5703f','#f2e2cc','#6b5a50','#463a33','#1d1816']),
'intro':('columns',6612,['#f3eee7','#fbf8f3','#7a4a2a','#5f534c','#2a2320']),
'r1':('arches',6621,['#efe8de','#dba077','#7a4a2a','#5f534c','#2a2320']),
'r2':('skyline',6622,['#2a2320','#bf7a48','#f4e6d2','#74635a','#4c3f38','#1f1a17']),
'g1':('hills',6631,['#e9e3d9','#ecd6bd','#dba077','#928883','#6b625d','#463f3b']),
'g2':('waves',6632,['#2a2320','#b5703f','#f2e2cc','#6b5a50','#463a33','#1d1816']),
'g3':('columns',6633,['#f3eee7','#fbf8f3','#7a4a2a','#5f534c','#2a2320']),
'g4':('arches',6634,['#2a2320','#bf7a48','#f4e6d2','#74635a','#4c3f38','#1f1a17'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Apartamentos Rosado · Apartamentos turísticos en Segovia, a 5 minutos del Acueducto',see_rooms='Ver apartamentos',hero_k='Segovia · Vía Roma, 15',hero_t='Segovia desde tu propio loft',hero_s='Cuatro apartamentos modernos y luminosos para 2 a 4 personas, a 5 minutos andando del Acueducto.',
 intro_t='Confort y relax',intro_p1='Cada apartamento tiene un diseño contemporáneo con salón-comedor, cocina totalmente equipada y dormitorio integrado con baño privado con ducha, cama de matrimonio y sofá cama.',
 intro_p2='Están en Vía Roma, en el tranquilo barrio de San Lorenzo, junto a la Alameda del Parral. A tu llegada te obsequian con un desayuno con café Lavazza.',
 stats=['4 apartamentos','De 2 a 4 personas','A 5 min del Acueducto','Wifi gratuito'],nav_rooms='Apartamentos',rooms_t='Los apartamentos',rooms_s='Todos con Smart TV, wifi gratuito, calefacción y aire acondicionado, ropa de cama y toallas.',
 svcs=['Cocina completa con menaje, tostadora y hervidor','Cafetera eléctrica Lavazza','Smart TV y wifi gratuito','Calefacción y aire acondicionado','Cuna bajo petición','Parada de autobús a 200 metros'],
 loc_p='Vía Roma, 15 · 40003 Segovia. Teléfono: 699 108 395. Correo: informacion@apartamentosrosado.es.',
 chips=['¿Qué apartamentos tenéis?','¿A qué hora es la entrada?','¿Admitís mascotas?','¿Cómo reservo?']),
'en':dict(title='Apartamentos Rosado · Holiday apartments in Segovia, 5 minutes from the Aqueduct',see_rooms='See apartments',hero_k='Segovia · Vía Roma, 15',hero_t='Segovia from your own loft',hero_s='Four modern, bright apartments for 2 to 4 people, a 5-minute walk from the Aqueduct.',
 intro_t='Comfort and relaxation',intro_p1='Each apartment has a contemporary design with a living-dining room, fully equipped kitchen and integrated bedroom with private shower room, double bed and sofa bed.',
 intro_p2='They are on Vía Roma, in the quiet San Lorenzo neighbourhood, next to the Alameda del Parral. On arrival you get a welcome breakfast with Lavazza coffee.',
 stats=['4 apartments','For 2 to 4 people','5 min from the Aqueduct','Free wifi'],nav_rooms='Apartments',rooms_t='The apartments',rooms_s='All with Smart TV, free wifi, heating and air conditioning, bed linen and towels.',
 svcs=['Full kitchen with utensils, toaster and kettle','Lavazza electric coffee machine','Smart TV and free wifi','Heating and air conditioning','Cot on request','Bus stop 200 metres away'],
 loc_p='Vía Roma, 15 · 40003 Segovia. Phone: +34 699 108 395. Email: informacion@apartamentosrosado.es.',
 chips=['Which apartments do you have?','What time is check-in?','Do you allow pets?','How do I book?']),
'fr':dict(title='Apartamentos Rosado · Appartements touristiques à Ségovie, à 5 minutes de l’aqueduc',see_rooms='Voir les appartements',hero_k='Ségovie · Vía Roma, 15',hero_t='Ségovie depuis votre loft',hero_s='Quatre appartements modernes et lumineux pour 2 à 4 personnes, à 5 minutes à pied de l’aqueduc.',
 intro_t='Confort et détente',intro_p1='Chaque appartement a un design contemporain avec séjour-salle à manger, cuisine entièrement équipée et chambre intégrée avec salle d’eau privée, lit double et canapé-lit.',
 intro_p2='Ils sont sur la Vía Roma, dans le quartier tranquille de San Lorenzo, près de l’Alameda del Parral. À votre arrivée, un petit-déjeuner avec café Lavazza vous est offert.',
 stats=['4 appartements','De 2 à 4 personnes','À 5 min de l’aqueduc','Wifi gratuit'],nav_rooms='Appartements',rooms_t='Les appartements',rooms_s='Tous avec Smart TV, wifi gratuit, chauffage et climatisation, linge de lit et serviettes.',
 svcs=['Cuisine complète avec ustensiles, grille-pain et bouilloire','Cafetière électrique Lavazza','Smart TV et wifi gratuit','Chauffage et climatisation','Lit bébé sur demande','Arrêt de bus à 200 mètres'],
 loc_p='Vía Roma, 15 · 40003 Ségovie. Téléphone : +34 699 108 395. E-mail : informacion@apartamentosrosado.es.',
 chips=['Quels appartements avez-vous ?','À quelle heure est l’arrivée ?','Acceptez-vous les animaux ?','Comment réserver ?']),
'de':dict(title='Apartamentos Rosado · Ferienapartments in Segovia, 5 Minuten vom Aquädukt',see_rooms='Apartments ansehen',hero_k='Segovia · Vía Roma, 15',hero_t='Segovia aus dem eigenen Loft',hero_s='Vier moderne, helle Apartments für 2 bis 4 Personen, 5 Gehminuten vom Aquädukt.',
 intro_t='Komfort und Erholung',intro_p1='Jedes Apartment ist modern gestaltet, mit Wohn-Esszimmer, voll ausgestatteter Küche und integriertem Schlafbereich mit eigenem Duschbad, Doppelbett und Schlafsofa.',
 intro_p2='Sie liegen an der Vía Roma im ruhigen Viertel San Lorenzo, nahe der Alameda del Parral. Bei Ankunft gibt es ein Willkommensfrühstück mit Lavazza-Kaffee.',
 stats=['4 Apartments','Für 2 bis 4 Personen','5 Min. zum Aquädukt','Kostenloses WLAN'],nav_rooms='Apartments',rooms_t='Die Apartments',rooms_s='Alle mit Smart-TV, kostenlosem WLAN, Heizung und Klimaanlage, Bettwäsche und Handtüchern.',
 svcs=['Voll ausgestattete Küche mit Geschirr, Toaster und Wasserkocher','Elektrische Lavazza-Kaffeemaschine','Smart-TV und kostenloses WLAN','Heizung und Klimaanlage','Kinderbett auf Anfrage','Bushaltestelle in 200 Metern'],
 loc_p='Vía Roma, 15 · 40003 Segovia. Telefon: +34 699 108 395. E-Mail: informacion@apartamentosrosado.es.',
 chips=['Welche Apartments gibt es?','Wann ist der Check-in?','Sind Haustiere erlaubt?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://apartamentosrosado.es/reservas/'
BOOK=dict(mode='engine',url=dict(es=R,en=R,fr=R,de=R))
D=dict(name='Apartamentos Rosado',ac='#2a2320',ac2='#7a4a2a',ac2_a11y='#653d22',book=BOOK,around=[],foot=FOOT,
 address='Vía Roma, 15 · 40003 Segovia',phones=['+34 699 108 395'],emails=['informacion@apartamentosrosado.es'],maps='Apartamentos Rosado, Avenida Vía Roma 15, 40003 Segovia',t=T)
META=dict(repo='demo-apartamentos-rosado-segovia',name='Apartamentos Rosado',legal_name='GALERIAS ROSADO SL, NIF B40213787 (aviso legal de su web)',registry_ids=['B40213787'],
 url='https://apartamentosrosado.es/',domain='apartamentosrosado.es',municipality='Segovia',province='Segovia',sector='apartamentos turísticos en Segovia',
 read_at='2026-11-02T09:13:00+01:00',created_at='2026-11-02T09:12:00+01:00',built_at='2026-11-02T09:30:00+01:00',audit_date='2026-11-02T09:13:00+01:00',
 rating=dict(value=5.0,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Apartamentos+Rosado/@40.951671,-4.1114638,17z'),
 book=dict(mode='engine',url=R,note='pagina de reservas propia de su web (boton Reservar) con el motor MrPlan incrustado: https://apartamentosrosado.es/reservas/, HTTP 200 (02/11/2026 09:14). Solo en espanol, mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Qué tienen los apartamentos?','K02'),('¿Hay desayuno?','K03'),('¿A qué hora es la entrada?','K04'),('¿Admitís mascotas?','K05'),('¿Dónde estáis?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Puedo cancelar?','K08'),('¿Qué ver en Segovia?','K09'),('¿Hay autobús cerca?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis cuna?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which apartments do you have?','K01'),('What do the apartments include?','K02'),('Is there breakfast?','K03'),('What time is check-in?','K04'),('Do you allow pets?','K05'),('Where are you?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Can I cancel?','K08'),('What to see in Segovia?','K09'),('Is there a bus nearby?','K10'),('What is your phone number?','K11'),('Do you have a cot?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),('Que comprennent les appartements ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('À quelle heure est l’arrivée ?','K04'),('Acceptez-vous les animaux ?','K05'),('Où êtes-vous ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('Puis-je annuler ?','K08'),('Que voir à Ségovie ?','K09'),('Y a-t-il un bus à proximité ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous un lit bébé ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Was bieten die Apartments?','K02'),('Gibt es Frühstück?','K03'),('Wann ist der Check-in?','K04'),('Sind Haustiere erlaubt?','K05'),('Wo liegen die Apartments?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Kann ich stornieren?','K08'),('Was kann man in Segovia besichtigen?','K09'),('Gibt es einen Bus in der Nähe?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Haben Sie ein Kinderbett?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
