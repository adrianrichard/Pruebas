# -*- coding: iso-8859-1 -*-

import times

# Format: "Location name", Latitude, Longitude, Time zone, Elevation in meters
# Latitude/Longitude: degrees and minutes are separated by commas
# No sign means North resp. East
# - sign means South resp. West
builtinLocations = [ \
   ("Aach",             47.50,   8.51,  1, 0),        \
   ("Aachen",           50.47, 6.05,   1,  0),         \
   ("Abidjan",                     5.11,    -4.01,  0, 0),     \
   ("Abilene, TX",                32.27,   -99.44, -6, 0),     \
   ("Abu Dhabi",                  24.20,   54.34,   4, 0),     \
   ("Acapulco",                   17.05, -100.08,  -6, 0),     \
   ("Accra",                       5.20,    -0.09,  0,  0),    \
   ("Addis Abeba",       9.09,   38.46,  3,  0),       \
   ("Adelsheim",        49.24,   9.23,  1,   0),       \
   ("Aden, Jemen",      12.47,   45.02,  3,   0),      \
   ("Agana, Guam",                13.29,  144.45,  10,   0),   \
   ("Agen",             44.12,   0.37,  1,   0),       \
   ("Ahrweiler", 50.33,   7.08,   1,  0),  \
   ("Aix-en-Provence",  43.32,   5.26,  1,   0),       \
   ("Aix-les-Bains",    45.42,   5.45,  1,    0),      \
   ("Akron, OH",                  41.05,   -81.31, -5,  0),    \
   ("Al-Manamah, Bharain",        26.13,   50.33,   3,   0),   \
   ("Albany, NY",                 42.39,   -73.45, -5,   0),   \
   ("Albuquerque, NM",            35.05,  -106.39, -7,   0),   \
   ("Alburquerque",     39.13, -7.00,    1,     0),    \
   ("Alexandria, Egypt",31.11,   29.56,  2,      0),   \
   ("Alexandria, Greece",         40.38,   22.31,   2,   0),   \
   ("Algiers",                    36.30,     3.00,  1,   0),   \
   ("Äli Bayramli, Aserbaidschan",39.56,   48.55,   4,   0),   \
   ("Alicante",         38.21, -0.29,    1,    0),     \
   ("Allentown, PA",    40.36,  -75.29, -5,     0),    \
   ("Altensteig",       48.35, 8.37,   1,     0),      \
   ("Altlandsberg",     52.33,  13.43,  1,     0),     \
   ("Altonna, Pennsylvania",      40.31,   -78.24, -5,   0),   \
   ("Amarillo, TX",               35.12,  -101.50, -6,    0),  \
   ("Amberg",           49.27, 11.52,  1,     0),      \
   ("Amersfoort",       52.09, 5.24,   1,      0),     \
   ("Amiens, France",             49.54,    2.18,     1,  0),  \
   ("Amman",           31.42, 35.53,     2,    0),     \
   ("Amsterdam",        52.22, 4.54,   1,      0),     \
   ("Anchorage, AK",    61.13, -149.53, -9,     0),    \
   ("Ancona",           43.38, 13.30,    1,     0),    \
   ("Andorra, Spain",             40.58,   -0.28,   1,   0),   \
   ("Angermünde",       53.01,  14.00,  1,       0),   \
   ("Angers, France",             47.28,   -0.33,     1,  0),  \
   ("Ankara",           39.56, 32.52,    2,     0),    \
   ("Anklam",           53.51,  13.41,  1,       0),   \
   ("Ann Arbor, MI",    42.18,  -83.45, -5,     0),    \
   ("Annaberg",         57.31,  13.26,  1,     0),     \
   ("Annecy",           45.54,   6.07,  1,     0),     \
   ("Ansbach",          49.17,  10.34,  1,      0),    \
   ("Antananarivo",              -18.31,    47.18,  3,   0),   \
   ("Antibes",          43.35,   7.07,  1,     0),     \
   ("Antwerpen",        51.13, 4.25,   1,      0),     \
   ("Apolda",           51.01,  11.31,  1,      0),    \
   ("Appenweier",                 48.32,    7.58,     1,  0),  \
   ("Ar-Rijad (Riyadh)", 24.38, 46.43,     3,     0),    \
   ("Arad",            46.11, 21.20,     2,     0),    \
   ("Arcachon",         44.37,  -1.12,  1,     0),     \
   ("Arlon",            49.41, 5.49,   1,      0),     \
   ("Arnheim",          52.01, 5.53,   1,       0),    \
   ("Arnstadt",         50.50,  10.57,  1,     0),     \
   ("Aschaffenburg",  49.59,   9.09,  1,   0),  \
   ("Aschersleben",     51.45,  11.27,  1,      0),    \
   ("Ashland, KY",                38.29,   -82.38, -5,   0),   \
   ("Ashlville, NC",              35.36,   -82.33, -5,    0),  \
   ("Asmara, Eritrea",            15.01,   38.30,   3,    0),  \
   ("Asti",             44.54, 8.12,     1,    0),     \
   ("Asuncion",        -25.16, -57.40,   -4,    0),    \
   ("Athen",            37.58, 23.43,    2,     0),    \
   ("Atlanta (Ga., US)",33.45,  -84.23,  -5,    0),    \
   ("Atlantic City, NJ",          39.22,   -74.26, -5,   0),   \
   ("Auckland",                  -36.53,   174.45, 12,   0),   \
   ("Augsburg",         48.23, 10.53,  1,      0),     \
   ("Augusta, GA",      33.29,  -81.57, -5,    0),     \
   ("Augusta, Georgia",           33.28,   -81.58, -5,   0),   \
   ("Augusta, Maine",             44.19,   -69.46, -5,   0),   \
   ("Aurich",           53.28, 7.29,   1,      0),     \
   ("Austin, TX",                 30.16,   -97.45, -6,  0),    \
   ("Bützow",           53.50,  11.59,  1,    0),      \
   ("Bacau",           46.34, 26.55,     2,     0),    \
   ("Bad Berka",        50.54,  11.17,  1,     0),     \
   ("Bad Cannstatt",    48.48,   9.12,  1,     0),     \
   ("Bad Freienwalde",  52.47,  14.01,  1,     0),     \
   ("Bad Gottleuba",    50.51,  13.56,  1,     0),     \
   ("Bad Kissingen",    50.12, 10.04,  1,      0),     \
   ("Bad Kreuznach",    49.52, 7.51,   1,      0),     \
   ("Bad Krozingen",    47.55,   7.43,  1,     0),     \
   ("Bad Mergenheim",   49.30,   9.46,  1,     0),     \
   ("Bad Mingolsheim",  49.14,   8.39,  1,     0),     \
   ("Bad Nauheim",      50.22, 8.44,   1,      0),     \
   ("Bad Rappenau",     49.19,   9.06,  1,     0),     \
   ("Bad Salzungen",    50.48,  10.13,  1,     0),     \
   ("Bad Wilznack",     52.57,  11.57,  1,     0),     \
   ("Bad Wimpfen",      49.14,   9.09,  1,     0),     \
   ("Baden-Baden",      48.46, 8.14,   1,      0),     \
   ("Baden, Austria",     48.00, 16.14,  1,     0),    \
   ("Baden, Switzerland",    47.29,  8.18,  1,    0),     \
   ("Baghdad, Iraq",    33.21,   44.25,  3,    0),     \
   ("Baiersdorf",       49.39,  11.01,  1,      0),    \
   ("Bakersfield, CA",            35.23,  -119.01, -8,   0),   \
   ("Baku, Aserbaidschan",        40.21,   49.49,   4,    0),  \
   ("Ballenstedt",      51.43,  11.14,  1,     0),     \
   ("Baltimore, MD",    39.17,  -76.37,  -5,    0),    \
   ("Bamako",                     12.24,    -7.35,  0,   0),   \
   ("Bamberg",          49.53, 10.53,  1,     0),      \
   ("Bangkok",         13.35, 100.29,    7,    0),     \
   ("Bangor, Maine",              44.48,   -68.46, -5,   0),   \
   ("Bangui",                      4.14,    18.22,  1,    0),  \
   ("Banjul",                     13.17,   -16.23,  0,   0),   \
   ("Barby",            51.58,  11.53,  1,    0),      \
   ("Barcelona",        41.23, 2.11,     1,    0),     \
   ("Basel",            47.38, 7.40,   1,      0),     \
   ("Baton Rouge, Louisiana",     30.27,   -91.11, -6,   0),   \
   ("Battle Creek, MI",           42.19,   -85.11, -5,    0),  \
   ("Bautzen",          51.11,  14.26,  1,    0),      \
   ("Bay City, MI",               43.36,   -83.53, -5,   0),   \
   ("Bayonne",          43.29,  -1.29,  1,    0),      \
   ("Bayreuth",         49.57, 11.35,  1,      0),     \
   ("Beaumont, TX",               30.05,   -94.06, -6,   0),   \
   ("Beelitz",          52.14,  12.58,  1,    0),      \
   ("Beersheba",                  31.15,    34.48,  2,  0),    \
   ("Beeskow",          52.10,  14.14,  1,    0),      \
   ("Beirut",          33.20, 35.23,     2,    0),     \
   ("Belfast",          54.35, -5.55,  0,      0),     \
   ("Belfort",          47.38,   6.52,  1,     0),     \
   ("Belgrad",         44.50, 20.30,     1,    0),     \
   ("Belleville",                 44.10,   -77.23, -5,   0),   \
   ("Bellingham, WA",             48.46,  -122.29, -8,    0),  \
   ("Belmonte",         40.22, -7.22,    0,     0),    \
   ("Belts, Moldova",             47.45,   27.55,   2,   0),   \
   ("Bendery, Moldova",           46.50,   29.28,   2,    0),  \
   ("Benfeld",          48.22,   7.36,  1,     0),     \
   ("Bentonville, Arkansas",36.22, -94.13,  -6,   0),     \
   ("Berdicev, Ukraine",          49.54,   28.36,     2,  0),  \
   ("Beregovoye, Ukraine",        44.54,   33.37,     2,  0),  \
   ("Bergen, The Netherlands",    51.37,    6.04,   1,   0),   \
   ("Berkeley, CA",               37.52,  -122.16, -8,    0),  \
   ("Berlin",           52.31, 13.23,  1,     0),      \
   ("Bern",             46.57, 7.26,   1,      0),     \
   ("Bernau",           47.48,  12.22,  1,     0),     \
   ("Bernburg",         51.48,  11.44,  1,     0),     \
   ("Bershad, Ukraine",           48.22,   29.32,     2,   0), \
   ("Besancon",         47.15,   6.02,  1,    0),      \
   ("Bethlehem, Pennsylvania",    40.37,   -75.23, -5,   0),   \
   ("Biarritz",         43.29,  -1.34,  1,    0),      \
   ("Biel (Bienne)",      47.10,  7.12,  1,   0),      \
   ("Bielefeld",        52.01, 8.31,   1,    0),       \
   ("Biesenthal",       52.46,  13.37,  1,    0),      \
   ("Billings, Montana",          45.47,  -108.30, -7,   0),   \
   ("Biloxi, Mississippi",        30.24,   -88.53, -6,   0),   \
   ("Binghamton, NY",             42.06,   -86.49, -5,   0),   \
   ("Birmingham",       52.30, -1.50,  0,     0),      \
   ("Birmingham, AL",   33.31,  -86.49, -6,    0),     \
   ("Birobidzan",       48.48, 132.57, 9,       0),    \
   ("Bischeim, France",           48.37,    7.45,     1,  0),  \
   ("Bischkek, Kirgistan",        43.01,   74.58,   6,    0),  \
   ("Bismark, N. Dakota",         46.48,  -100.47, -7,    0),  \
   ("Blackpool",        53.50,  -3.03,  0,    0),      \
   ("Bleicherode",      51.26,  10.34,  1,    0),      \
   ("Bloomington, IL",            40.29,   -89.00, -6,   0),   \
   ("Boca Raton, FL",   26.21,  -80.05, -5,    0),     \
   ("Bogota",         4.36,  -74.05,    -5,    0),     \
   ("Boise, Idaho",               43.37,  -116.12, -7,   0),   \
   ("Boizenburg",       53.22,  10.43,  1,     0),     \
   ("Bologna",          44.29, 11.20,    1,    0),     \
   ("Bombay, India (GMT+5)",18.58,  72.50,  5,    0),     \
   ("Bombay, India (GMT+6)",18.58,  72.50,  6,    0),     \
   ("Bonn",             50.44, 7.06,   1,     0),      \
   ("Boras",           57.43, 12.55,     1,   0),      \
   ("Bordeuax",         44.50,  -0.34,  1,     0),     \
   ("Borna",            51.19,  13.11,  1,     0),     \
   ("Boston, MA",       42.21,  -71.04,  -5,   0),     \
   ("Botosani",        47.45, 26.40,     2,    0),     \
   ("Boulay-Moselle",   49.11,   6.30,  1,      0),    \
   ("Boulogne-Sur-Mer", 50.43,   1.37,  1,     0),     \
   ("Bournemouth",      50.43,  -1.54,  0,     0),     \
   ("Bowling Green, KY",          37.00,   -86.27, -5,   0),   \
   ("Brüel",            53.44,  11.43,  1,    0),      \
   ("Brünn",           49.12, 16.37,     1,   0),      \
   ("Brüssel",          50.50, 4.20,   1,     0),      \
   ("Bradford",         53.48, -1.45,  0,     0),      \
   ("Brandenburg",      52.24, 12.32,  1,     0),      \
   ("Brandon",                    49.51,   -99.57, -6,   0),   \
   ("Brantford",                  43.09,   -80.16, -5,   0),   \
   ("Brasilia",                  -15.10,  -47.54,  -3,   0),   \
   ("Brasov",          45.39, 25.37,     2,    0),     \
   ("Bratislava",      48.09, 17.07,     1,    0),     \
   ("Brattleboro, VT",            42.51,   -72.34, -5,   0),   \
   ("Braunschweig",     52.16, 10.31,  1,     0),      \
   ("Brazzaville",                -4.08,    15.08,  1,   0),   \
   ("Breisach",         48.01,   7.40,  1,    0),      \
   ("Bremen",           53.04, 8.49,   1,     0),      \
   ("Bremerhaven",      53.33, 8.34,   1,     0),      \
   ("Bremgarten",       47.21, 8.21,   1,     0),      \
   ("Brest, Fr.",       48.24,  -4.29,  1,    0),      \
   ("Bridgeport",                 41.11,   -73.11, -5,  0),    \
   ("Bridgetown (Barbados)",      13.05,  -59.28,  -4,  0),    \
   ("Brighton",         50.50,  -0.08,  0,     0),     \
   ("Brisbane",       -27.28, 153.02,   10,    0),     \
   ("Bristol",          51.27, -2.35,  0,      0),     \
   ("Brno",                       49.12,   16.35,   1,   0),   \
   ("Brockton, MA",               42.05,   -71.01, -5,   0),   \
   ("Broken Hill, Australia",    -31.52,  141.10,  10,   0),   \
   ("Brownsville, TX",            25.54,   -97.30, -6,   0),   \
   ("Buchara",          39.46,   64.25,  5,   0),      \
   ("Budapest",        47.30, 19.05,     1,   0),     \
   ("Buenos Aires",    -34.36, -58.27,   -3,  0),    \
   ("Buffalo",          42.54,  -78.53,  -5,  0),   \
   ("Buffalo, NY",                42.53,   -78.52, -5,   0),   \
   ("Bujumbura",                  -3.13,    29.11,  2,   0),   \
   ("Bukarest",        44.26, 26.06,     2,    0),     \
   ("Bukavu, Zaire",              -2.33,   28.39,   2,   0),   \
   ("Burg",             52.16,  11.51,  1,    0),      \
   ("Burlington (VT, US)", 44.29,  -73.13,  -5,    0),    \
   ("Burlington",                 43.20,   -79.48, -5,  0),    \
   ("Bursa",            40.11, 29.04,    2,   0),      \
   ("Bussum",           52.16, 5.10,   1,      0),     \
   ("Butte, Montana",             46.01,  -112.32, -7,   0),   \
   ("Caen",             49.11,  -0.21,  1,     0),     \
   ("Cahul, Moldova",             45.54,   28.12,   2,  0),    \
   ("Calabasas, AZ",       31.28, -110.58, -7,   0),   \
   ("Calabasas, CA",       34.09, -118.38, -8,     0),
   ("Calbe",            51.54,  11.46,  1,     0),     \
   ("Calgary",                    51.03,  -114.03, -7,   0),   \
   ("Cali",           3.27,  -76.31,    -5,   0),      \
   ("Caluire et Cuire", 45.48,   4.51,  1,    0),      \
   ("Calvörde",         52.23,  11.17,  1,    0),      \
   ("Calw",             48.43, 8.44,   1,     0),      \
   ("Cambridge",        52.13,   0.08,  0,    0),      \
   ("Cambridge, MA",              42.22,   -71.06, -5,    0),  \
   ("Camdon, NJ",                 39.57,   -75.07, -5,    0),  \
   ("Canberra",       -35.17, 149.08,   10,   0),      \
   ("Cannes",           43.33,   7.01,  1,    0),      \
   ("Canton, Ohio",     40.48,  -81.22,  -5,  0),      \
   ("Capetown, South Africa",-33.55, 18.22, 2,   0),      \
   ("Caputh",           52.21,  13.00,  1,       0),   \
   ("Caracas, Venezuela",  10.30, -66.56, -4,    0),      \
   ("Carpentras",       44.03,   5.03,  1,       0),   \
   ("Carson City, NV",            39.10,  -119.46, -8,  0),    \
   ("Cartagena, Spain",    37.36, -0.59,  1,    0), \
   ("Casablanca, Marokko", 33.39,   -7.35,  0,    0),     \
   ("Cavaillon",        43.50,   5.02,  1,      0),    \
   ("Cayenne (French - Guyana)",   4.47,   52.28,  -3,   0),   \
   ("Cebu, Phillipines",          10.11,  123.45,   8,   0),   \
   ("Cedar Grove, NJ (1)", 40.51, -74.14,  -5,  0), \
   ("Cedar Grove, NJ (2)", 39.58, -74.10,  -5,  0), \
   ("Cedar Rapids, IA",           41.58,   -91.40, -6,   0),   \
   ("Celle",            52.37, 10.05,  1,    0),       \
   ("Central Islip, NY",          40.47,   -73.12, -5,   0),   \
   ("Chalkis, Greece",            38.28,   23.36,   2,   0),  \
   ("Chalons-Sur-Marne",48.57,   4.22,  1,    0),      \
   ("Chalons-Sur-Saone",46.47,   4.51,  1,    0),      \
   ("Chambery, France",           45.34,    5.65,     1,  0),  \
   ("Champaign, IL",              40.07,   -88.15, -6,    0),  \
   ("Chapel Hill, NC",  35.55,  -79.04, -5,    0),     \
   ("Charkow, Ukraine",           49.55,   36.10,     2,   0), \
   ("Charleroi",        50.25, 4.26,   1,     0),      \
   ("Charleston (S.C., US)",32.48, -79.57,  -5,    0),    \
   ("Charleston, West Virginia",  38.21,   -81.38, -5,  0),    \
   ("Charlotte (N.C., US)", 35.14,  -80.50,  -5,  0),  \
   ("Charlottesville, Virginia",    38.02, -78.29, -5,   0),  \
   ("Chattanooga (Tenn., US)",    35.03,   -85.19, -6,   0),   \
   ("Chemnitz",         50.50, 12.55,  1,     0),      \
   ("Chernigov, Ukraine",         50.50,   24.08,     2,  0),  \
   ("Cherson, Ukraine",           46.39,   32.36,     2,  0),  \
   ("Cheyenne, Wyoming",          41.08,  -104.49, -7,  0),    \
   ("Chicago",          41.53,  -87.38,  -6,   0),     \
   ("Churchill",                  58.45,   -94.10, -6,   0),   \
   ("Cincinnati, OH",   39.06,  -84.38,  -5,   0),     \
   ("Clermont-Ferrand", 45.47,   3.05,  1,     0),     \
   ("Cleveland (Ohio, US)",41.30,  -81.41,  -5,    0),    \
   ("Cluj",            46.47, 23.36,     2,     0),    \
   ("Coesfeld",         51.56,   7.10,  1,      0),    \
   ("Colmar",           58.05,   7.22,  1,      0),    \
   ("Columbia, Missouri",         38.57,   -92.20, -6,   0),   \
   ("Columbia, SC",               34.00,   -81.02, -5,   0),   \
   ("Columbus, Georgia",          32.28,   -84.59, -5,   0),   \
   ("Columbus, OH",     39.57,  -83.00,  -5,   0),     \
   ("Conakry",                     9.19,    13.10,  0,   0),   \
   ("Concord, New Hampshire",     43.12,   -71.32, -5,   0),   \
   ("Constanta",       44.11, 28.39,     2,    0),     \
   ("Cordoba, Argentinia",       -31.09,  -64.15,  -3,   0),   \
   ("Cordoba, Spain",             57.52,   -4.50,   1,   0),   \
   ("Cordova, Alaska, U.S.A.",    60.33, -145.45,  -9,   0),   \
   ("Corpus Christi, TX",         27.48,   -97.24, -6,   0),   \
   ("Coswig",           51.53,  12.26,  1,   0),       \
   ("Cottbus",          51.45, 14.19,  1,    0),       \
   ("Coventry",         52.25,  -1.30,  0,   0),       \
   ("Crivitz",          53.35,  11.38,  1,   0),       \
   ("Crossen",          50.45, 12.29,  1,    0),       \
   ("Croydon",          51.23,  -0.06,  0,   0),       \
   ("Czernowitz, Chernovtsy, Ukraine",48.17,25.58,    2,  0),  \
   ("Dömitz",           53.08,  11.14,  1,     0),     \
   ("Düsseldorf",       51.12, 6.47,   1,      0),     \
   ("Dachau",           48.15, 11.27,  1,      0),     \
   ("Dakar",                      14.23,   -17.16,  0,   0),   \
   ("Dakar, Senegal",             14.47,  -16.57,   0,   0),   \
   ("Dalian, China",              38.55,  121.39,   8,   0),   \
   ("Dallas, TX",       32.47,  -96.48,  -6,   0),     \
   ("Damaskus",        33.08, 36.26,     3,    0),     \
   ("Daressalam",                 -6.31,    39.11,  3,  0),    \
   ("Dargun",           53.54,  12.51,  1,   0),       \
   ("Darmstadt",        49.53, 8.40,   1,     0),      \
   ("Davenport, IA",              41.31,   -90.35, -6,   0),   \
   ("Davos",              46.48,  9.50,  1,   0),      \
   ("Dawson",                     64.04,  -139.26, -8,   0),   \
   ("Dayton, OH",                 39.46,   -84.12, -5,   0),   \
   ("Daytona Beach, FL",          29.13,   -81.01, -5,    0),  \
   ("Deauville, France",          49.22,    0.04,     1,  0),  \
   ("Decatur, IL",                39.51,   -88.57, -6,    0),  \
   ("Decin",                      50.48,   14.13,     1,  0),  \
   ("Deggendorf",       48.51,  12.59,  1,    0),      \
   ("Delitzsch",        51.31,  12.20,  1,    0),      \
   ("Demmin",           53.54,  13.02,  1,    0),      \
   ("Den Haag",         52.06, 4.18,   1,      0),     \
   ("Denver (Colo., US)", 39.43, -105.01,  -7,    0),    \
   ("Denzlingen",                 48.04,    7.52,   0,   1),   \
   ("Desmoines, IA",    41.35,  -93.37, -6,    0),     \
   ("Dessau",           51.50, 12.14,  1,      0),     \
   ("Detroit, MI",      42.20,  -83.03,  -5,    0),    \
   ("Dhaka, Bangladesh",          23.29,   90.24,   6,  0),    \
   ("Dieburg",          49.54,   8.50,  1,     0),     \
   ("Dieuze, France",             48.49,    6.43,     1,  0),  \
   ("Dijon",            47.19,   5.01,  1,     0),     \
   ("Djakarta, Indonesia", -6.10,  106.48,  7,     0),    \
   ("Dnepropetrovsk, Ukraine",    48.27,   35.02,     2,  0),  \
   ("Dodge City (Kans., US)",     37.45,  -100.01, -6,   0),   \
   ("Donetsk, Ukraine",           48.00,   37.48,     2,  0),  \
   ("Dorohoi",         47.57, 26.24,     2,    0),     \
   ("Dortmund",         51.31, 7.28,   1,      0),     \
   ("Drama, Greece",              41.09,   24.10,   2,  0),    \
   ("Dresden",          51.03, 13.44,  1,     0),      \
   ("Dubayy",           25.18,   55.18,  4,   0),      \
   ("Dublin",           53.20, -6.15,  0,     0),      \
   ("Dubrovnik",       42.38, 18.07,     1,   0),      \
   ("Dubuque, IA",                42.30,   -90.40, -6,  0),    \
   ("Duisburg",         51.25, 6.46,   1,       0),    \
   ("Duluth, Minnesota",          46.47,   -92.06, -6,  0),    \
   ("Dunkerque, France",          51.03,    2.22,     1,  0),  \
   ("Durban, South Africa",      -29.52,   30.54,   2,  0),    \
   ("Durham, NC",                 36.00,   -78.55, -5,  0),    \
   ("Durlach",          49.00,   8.28,  1,    0),      \
   ("Durres, Albania",  41.19,   19.26,  1,   0),      \
   ("Dushanbe, Tadschikistan",    38.36,   69.06,   6,   0),   \
   ("Eastbourne",       50.46,   0.17,  0,    0),      \
   ("Eau Claire (Wis., US)",      44.49,   -91.30, -6,  0),    \
   ("Edinburgh",        55.57, -3.13,  0,      0),     \
   ("Edmondton",                  53.33,  -113.29, -7,  0),    \
   ("Eilat",            29.33, 34.57,  2,      0),     \
   ("Eindhoven",        51.26, 5.28,   1,      0),    \
   ("El Paso, TX",                31.46,  -106.29, -6,  0),    \
   ("Elbeuf, France",             49.17,    1.00,     1,  0),  \
   ("Elizabeth, N.J, US",  40.40, -74.11, -5,    0),      \
   ("Emmendingen",      48.07, 7.50,   1,     0),      \
   ("Encinitas, CA",       33.02, -117.17, -8,   0),   \
   ("Enid, Oklahoma",             36.24,   -97.53, -6,   0),   \
   ("Enschede",         52.12, 6.53,   1,   0),        \
   ("Epernay, France",            49.03,    3.57,     1,  0),  \
   ("Epinal, France",             48.11,    6.27,     1,  0),  \
   ("Er Riad",                    24.39,   46.42,   3,   0),   \
   ("Erfurt",           50.58, 11.01,  1,     0),      \
   ("Erie, Pennsylvania",         42.07,   -80.05, -5,   0),   \
   ("Esch-sur-Alzette",49.30, 5.59,      1,   0),      \
   ("Essen/Ruhr",       51.28, 7.01,   1,     0),      \
   ("Essexville, MI",   43.37,  -83.50,  -5,  0),      \
   ("Ettenheim",                  48.15,    7.49,     1,  0),  \
   ("Eugene (Oreg, US)",          44.03,  -123.06, -8,   0),   \
   ("Eureka, CA",                 40.48,  -124.10, -8,   0),   \
   ("Evansville, Indiana",        37.58,   -87.34, -6,   0),   \
   ("Evian-Les-Bains",  46.23,   6.35,  1,    0),      \
   ("Exeter",           50.43,  -3.31,  0,    0),      \
   ("Fürth",            49.28, 10.59,  1,     0),      \
   ("Fairbanks, AK",    64.51, -147.43, -10,  0),      \
   ("Fall River, MA",             41.42,   -71.09, -5,  0),    \
   ("Fargo, N. Dakota",           46.53,   -96.47, -7,  0),    \
   ("Ferrara",          44.50, 11.35,    1,   0),      \
   ("Firenze, Italy",             43.46,   11.14,   1,   0),   \
   ("Flagstaff, Arizona",  35.12, -111.39,  -7,   0),     \
   ("Flint, MI",                  43.01,   -83.42, -5,  0),    \
   ("Florenz",          43.46, 11.15,    1,   0),      \
   ("Florina",                    40.47,   21.25,   2,  0),    \
   ("Forbach, France",            49.11,    6.54,     1,  0),  \
   ("Fort Lauderdale, FL", 26.07,  -80.08, -5,    0),     \
   ("Frankfurt/Main",   50.07, 8.40,   1,     0),      \
   ("Frankfurt/Oder",   52.20, 14.33,  1,     0),      \
   ("Fredericton",                45.58,   -66.39, -4,  0),    \
   ("Freetown, Sierra Leone",      8.30,  -13.13,   0,  0),    \
   ("Freiburg i. Br.",  47.59, 7.51,   1,    0),       \
   ("Fresno, CA",                 36.44,  -119.47, -8,   0),   \
   ("Ft Smith, Arkansas",         35.23,   -94.26, -6,   0),   \
   ("Ft Worth, TX",               32.45,   -97.20, -6,   0),   \
   ("Ft. Walton Beach, FL",30.24,  -86.31, -5,   0),      \
   ("Ft. Wayne, Indiana",         41.04,   -85.08, -6,  0),    \
   ("Fulda",            50.33, 9.41,   1,     0),      \
   ("Göteborg",        57.43, 11.58,     1,  0),       \
   ("Göttingen",        51.32, 9.55,   1,    0),       \
   ("Gaborone",                  -24.27,    25.33,  2,  0),    \
   ("Gadsten, AL",                34.01,   -86.01, -6,  0),    \
   ("Gainesville, FL",            29.39,   -82.19, -5,  0),    \
   ("Galanta",         48.12, 17.43,     1,   0),      \
   ("Galati",          45.26, 28.03,     2,   0),      \
   ("Gallup, NM",                 35.31,  -108.44, -7,   0),   \
   ("Galveston, TX",              29.18,   -94.48, -6,   0),   \
   ("Gap, France",                44.34,    6.05,     1,  0),  \
   ("Gary, Indiana",              41.37,   -87.20, -6,  0),    \
   ("Gateshead",        54.58, -1.37,  0,    0),       \
   ("Gelsenkirchen",    51.31, 7.07,   1,    0),       \
   ("Geneve",           46.12, 6.09,   1,    0),       \
   ("Gent",             51.03, 3.43,   1,    0),       \
   ("Genua",            44.25, 8.57,     1,     0),    \
   ("Georgetown, Gambia",         13.13,  -14.45,   0,  0),    \
   ("Gießen",           50.35, 8.40,   1,    0),       \
   ("Givat Zev, Israel",   31.51, 35.09,  2,    0), \
   ("Glasgow",          55.53, -4.15,  0,     0),      \
   ("Gondar, Ethiopia", 12.36,   37.30,  3,   0),      \
   ("Grabow",           53.16, 11.34,  1,     0),      \
   ("Grand Junction",             39.04,  -108.34, -7,   0),   \
   ("Grand Rapids, MI",           42.58,   -85.40, -5,   0),   \
   ("Grasse",           43.40,   6.55,  1,    0),      \
   ("Graz",             47.05, 15.27,  1,     0),      \
   ("Great Falls, Montana",       47.30,  -111.18, -7,  0),    \
   ("Green Bay (Wis., US)",       44.31,   -88.01, -6,  0),    \
   ("Greensboro, NC",             36.04,   -79.47, -5,  0),    \
   ("Greenville, SC",             34.51,   -82.24, -5,  0),    \
   ("Greenwich Meridian",   0.00,    0.00,  0,   0),      \
   ("Grenoble",         45.10,   5.43,  1,       0),   \
   ("Grimsby",          53.35,  -0.05,  0,       0),   \
   ("Groningen",        53.13, 6.33,   1,        0),   \
   ("Guangzhou (Canton)", 23.06, 113.16, 8,      0),   \
   ("Guatemala City",             14.35,  -90.40,  -6,  0),    \
   ("Guelph",                     43.33,   -80.15, -5,  0),    \
   ("Guildford",        51.14,  -0.35,  0,   0),       \
   ("Gulfport, Mississippi",      30.22,   -89.06, -6,   0),   \
   ("Hagen (Westf)",    51.22, 7.28,   1,     0),      \
   ("Hagenow", 53.26,   11.11,   1,   0),    \
   ("Haguenau",         48.49,   7.47,  1,     0),     \
   ("Haifa",            32.22, 34.56,  2,      0),     \
   ("Halifax, N.S., Can.", 44.39, -63.36, -4,  0),     \
   ("Halle/Saale",      51.29, 11.58,  1,      0),     \
   ("Hamburg",          53.33, 9.59,   1,      0),     \
   ("Hameln",           52.06, 9.21,   1,      0),     \
   ("Hamilton",                   43.15,   -79.53, -5,   0),   \
   ("Hamilton, OH",               39.24,   -84.34, -5,   0),   \
   ("Hannover",         52.24, 9.44,   1,     0),      \
   ("Hanoi",                      21.04,   105.50,  7,   0),   \
   ("Harare",                    -17.30,    31.02,  2,   0),   \
   ("Harlow",           51.47,   0.08,  0,    0),      \
   ("Harrisburg, Pennsylvania",   40.16,   -76.53, -5,   0),   \
   ("Harrogate",        54.00,  -1.33,  0,     0),     \
   ("Harrow, United Kingdom",     51.35,   -0.22,     0,  0),   \
   ("Hartford (Conn., US)",41.46,  -72.41,  -5,   0),     \
   ("Havana",         23.08, -82.22,    -5,    0),     \
   ("Havelberg",        52.50, 12.04,  1,      0),    \
   ("Hebron",           31.32, 35.06,  2,      0),    \
   ("Heidelberg",       49.25, 8.43,   1,      0),    \
   ("Helena, Montana",            46.36,  -112.02, -7,  0),    \
   ("Helsinki",        60.10, 24.58,     2,     0),    \
   ("Hemel Hempstead",  51.46,  -0.28,  0,      0),    \
   ("Herford",          52.06, 8.40,   1,       0),    \
   ("Hermosillo, Mexico",         29.11, -110.59,  -6,   0),   \
   ("Hessisch Oldendorf",52.10, 9.15,   1,   0),        \
   ("Hildesheim",       52.09, 9.57,   1,    0),       \
   ("Hilo",                       19.44,  -155.05, 10,  0),    \
   ("Hilversum",        52.14, 5.10,   1,    0),       \
   ("Hof",              50.18, 11.55,  1,    0),       \
   ("Hollywood",        26.00,  -80.09,  -5,    0),    \
   ("Holyoke, MA",                42.12,   -72.37, -5,   0),   \
   ("Hongkong",        25.15, 114.10,    8,   0),      \
   ("Honolulu",       21.19, -157.50,   -10,  0),      \
   ("Houston, TX",      29.46,  -95.22,  -6,  0),      \
   ("Hove",             50.49,  -0.10,  0,    0),      \
   ("Hull",                       45.26,   -75.43, -5,  0),    \
   ("Huntington, West Virginia",  38.25,   -82.27, -5,  0),    \
   ("Huntsville, AL",             34.44,   -86.35, -6,  0),    \
   ("Iasi",            47.10, 27.35,     2,    0),     \
   ("Idar-Oberstein",   49.42, 7.19,   1,      0),     \
   ("Indianapolis, Indiana", -19.02,  -47.55,  -6,  0),   \
   ("Ingwiller, France",          48.52,    7.29,     1,  0),  \
   ("Innsbruck",        47.16, 11.24,  1,    0),       \
   ("Iowa City, IA",              41.40,   -91.32, -6,  0),    \
   ("Irkutsk",          52.16, 104.20, 8,    0),       \
   ("Istanbul",         41.01, 28.58,    2,  0),       \
   ("Izmir",            38.25, 27.09,    2,  0),       \
   ("Jackson, MI",                42.15,   -84.24, -5,   0),   \
   ("Jackson, Mississippi",       32.18,   -90.11, -6,   0),   \
   ("Jacksonsville, FL",30.20,  -81.40, -5,   0),      \
   ("Jakarta, Indonesia",         -6.17,  106.39,   7,   0),   \
   ("Jekaterinburg",    56.50,   60.30,  5,    0),     \
   ("Jersey City, NJ",            40.44,   -74.04, -5,  0),    \
   ("Jerusalem",        31.24, 35.00,  2,    0),       \
   ("Johannesburg",    -26.15, 28.00,    2,  0),       \
   ("Johnstown, Pennsylvania",    40.20,   -78.55, -5,   0),   \
   ("Joplin, Missouri",           37.05,   -94.30, -6,   0),   \
   ("Juneau, AK",                 58.18,  -134.25, -10,  0),   \
   ("Köln",             50.56, 6.59,   1,     0),      \
   ("Königs Wusterhausen",        52.18,   13.37,     1,  0),  \
   ("Königsberg",       54.43,  20.30,  2,     0),     \
   ("Kaifeng, China",   34.48,  114.26,  8,    0),     \
   ("Kairo",           29.40, 31.01,     2,    0),     \
   ("Kaiserslautern",   49.26, 7.46,   1,      0),     \
   ("Kalamazoo, MI",              42.17,   -85.35, -5,   0),   \
   ("Kampala",                     0.12,    32.21,  3,   0),   \
   ("Kanarische Inseln",          28.28,  -15.03,   0,   0),   \
   ("Kansas City (Kans., US)", 39.07, -94.39, -6,   0),   \
   ("Kansas City, Missouri",      39.05,   -94.35, -6,   0),   \
   ("Kapstadt (Capetown)", -33.55, 18.22,  2,    0),      \
   ("Karachi",          24.52,   67.03,  5,      0),   \
   ("Karlovy Vary",               50.11,   12.52,     1,  0),  \
   ("Karlsbad",        50.11, 12.52,     1,     0),    \
   ("Karlsruhe",        49.03, 8.24,   1,       0),    \
   ("Kassel",           51.19, 9.29,   1,       0),    \
   ("Katmandu, Nepal",            27.40,   85.28,   6,   0),   \
   ("Kaunas",           54.54,  23.54,  2,     0),     \
   ("Kehl",                       48.35,    7.50,     1,  0),  \
   ("Kenosha (Wis., US)",         42.36,   -87.50, -6,    0),  \
   ("Kenzingen",                  48.11,    7.46,     1,  0),  \
   ("Key West, FL",               24.34,   -81.48, -5,    0),  \
   ("Khabarovsk, Russia",         48.04,  134.38,  10,    0),  \
   ("Khartoum",                   15.20,    32.13,  2,    0),  \
   ("Khartoum, Sudan",            15.14,   32.34,   2,    0),  \
   ("Kiel",             54.20, 10.08,  1,    0),       \
   ("Kiew",             50.26, 30.31,  2,    0),       \
   ("Kigali",                     -1.34,     3.02,  2,   0),   \
   ("Kilkis, Greece",             41.00,   22.54,   2,   0),   \
   ("Kingston",                   44.14,   -76.29, -5,   0),   \
   ("Kinshasa",                   -4.11,    15.11,  1,   0),   \
   ("Kishinew, Moldova",          47.00,   28.50,   2,   0),   \
   ("Kitchener",                  43.27,   -80.29, -5,   0),   \
   ("Kleinmachnow",     52.24, 13.15,  1,     0),      \
   ("Knokke",           51.21, 3.17,   1,     0),      \
   ("Knoxville (Tenn., US)",      35.58,   -83.55, -6,   0),   \
   ("Koblenz",          50.21, 7.35,   1,     0),      \
   ("Konstanz",            47.04,  9.10,  1,    0), \
   ("Kopenhagen",      55.40, 12.35,     1,   0),      \
   ("Korfu",            39.36, 19.56,    2,   0),      \
   ("Korosten, Ukraine",          50.57,   28.38,     2,  0),  \
   ("Kosice",          48.43, 21.15,     1,    0),     \
   ("Krakau",           50.03, 19.58,  1,      0),     \
   ("Krasnojarsk",      56.00,   92.59,  7,    0),     \
   ("Krefeld",          51.20, 6.34,   1,      0),     \
   ("Kremenchug, Ukraine",        49.04,   33.25,     2,  0),  \
   ("Kuala Lumpur, Malaysia",3.09, 101.43,  8,     0),    \
   ("Kuwait, Kuwait",   29.30,   47.45,  3,     0),    \
   ("Lörrach",          47.37, 7.40,   1,       0),    \
   ("Lübeck",           53.52, 10.40,  1,       0),    \
   ("La Chaux-De-Fonds",  47.06,  6.50,  1,     0),    \
   ("La Ciotat, France",          43.10,    5.36,     1,  0),  \
   ("La Paz, Argentinia",        -30.45,  -59.40,  -3,    0),  \
   ("La Plata, Argentinia",      -34.58,  -57.58,  -3,    0),  \
   ("La Rochelle",      46.10,  -1.10,  1,     0),     \
   ("La Salle",                   45.26,   -73.40, -5,   0),   \
   ("La Seyne-Sur-Mer", 43.06,   5.53,  1,      0),    \
   ("Laayoune",                   27.06,   -13.07,  1,   0),   \
   ("Lafayette, Indiana",         40.25,   -86.54, -6,   0),   \
   ("Lagos",                       6.16,     3.17,  1,   0),   \
   ("Lagos, Nigeria",    6.27,    3.24,  1,    0),     \
   ("Lahr",                       48.20,    7.52,     1,  0),  \
   ("Lancaster, Pennsylvania",    40.02,   -76.18, -5,    0),  \
   ("Landau an der Isar", 48.40,  12.43,  1,    0),      \
   ("Landau",           49.12,   8.07,  1,      0),    \
   ("Lansing, MI",                42.44,   -84.33, -5,   0),   \
   ("Laredo, TX",                 27.30,   -99.31, -6,   0),   \
   ("Larissa, Greece",            39.38,   22.25,   2,   0),   \
   ("Las Vegas, NV",    36.11, -115.08, -8,    0),     \
   ("Lausanne",         46.31, 6.38,   1,      0),     \
   ("Laval",                      45.13,   -73.45, -5,  0),    \
   ("Lawrence, MA",               42.42,   -71.10, -5,  0),    \
   ("Le Havre",         49.30,   0.08,  1,    0),      \
   ("Le Mans, France",            48.00,    0.12,     1,  0),  \
   ("Leeds",            53.50, -1.35,  0,     0),      \
   ("Leicester",        52.38,  -1.05,  0,    0),      \
   ("Leiden",           52.09, 4.30,   1,     0),      \
   ("Leipzig",          51.19, 12.20,  1,     0),      \
   ("Lemberg, Lwow, Ukraine",     49.50,   24.02,     2,  0),  \
   ("Lethbridge",                 49.42,  -112.50, -7,    0),  \
   ("Lexington, KY",              38.03,   -84.30, -5,    0),  \
   ("Lhasa",                      29.41,    92.12,  8,    0),  \
   ("Liberec",         50.46, 15.03,     1,    0),     \
   ("Libourne, France",           44.55,   -0.14,     1,  0),  \
   ("Libreville",                  0.14,     9.15,  1,    0),  \
   ("Lihue",                      21.59,  -159.23, 10,    0),  \
   ("Lille",            50.38,   3.04,  1,    0),      \
   ("Lilongwe",                  -13.35,    33.29,  2,   0),   \
   ("Lima",           -12.03, -77.03,   -5,    0),     \
   ("Lima, OH",                   40.45,   -84.06, -5,   0),   \
   ("Limerick, Ireland",          52.42,   -8.40,   0,   0),   \
   ("Limoges",          45.50,   1.16,  1,      0),    \
   ("Lincoln, Nebraska",          40.49,   -96.42, -6,  0),    \
   ("Linz",             48.18, 14.18,  1,      0),     \
   ("Lissabon",         38.43, -9.08,    0,    0),     \
   ("Little Rock",      34.44,  -92.15,  -6,   0),     \
   ("Liége",            50.38, 5.34,   1,      0),     \
   ("Liverpool",        53.25, -2.55,  0,      0),     \
   ("Livorno",          43.33, 10.19,    1,    0),     \
   ("Ljubljana",       46.03, 14.31,     1,    0),     \
   ("Lodz",             51.46, 19.13,  1,      0),     \
   ("Logan, Utah",                41.44,  -111.50, -7,  0),    \
   ("Lome",                        6.06,     1.13,  0,  0),    \
   ("London",           51.30, -0.10,  0,      0),     \
   ("London, Ontario",            42.59,   -81.14, -5,   0),   \
   ("Long Beach, CA",             33.46,  -118.11, -8,   0),   \
   ("Lorain, OH",                 41.28,   -82.11, -5,   0),   \
   ("Los Angeles (LA)", 34.03, -118.15,  -8,     0),   \
   ("Louisville (Ky., US)",38.16,  -85.45,  -5,     0),   \
   ("Lowell, MA",                 42.38,   -71.19, -5,  0),    \
   ("Luanda",                     -8.30,    13.09,  1,  0),    \
   ("Lubbock, TX",                33.35,  -101.51, -6,  0),    \
   ("Ludwigshafen",     49.29, 8.26,   1,     0),      \
   ("Ludwigslust",      53.19, 11.30,  1,     0),      \
   ("Lugano",             46.01,  8.58,  1,   0),      \
   ("Lugoj, Romania",   45.41,   21.54,  2,   0),      \
   ("Lund",            55.42, 13.11,     1,   0),      \
   ("Luneville, France",          48.36,    6.30,     1,  0),  \
   ("Lusaka",                    -15.17,    28.10,  2,    0),  \
   ("Lushnje, Albania", 40.56,   19.42,  1,    0),     \
   ("Luton",            51.53,  -0.25,  0,     0),     \
   ("Luxemburg",       49.36, 6.09,      1,    0),     \
   ("Luzern",             47.03,  8.18,  1,    0),     \
   ("Lyon",             45.45,   4.51,  1,     0),     \
   ("Mönchengladbach",  51.12, 6.28,   1,      0),     \
   ("Mülhausen im Täle",48.34,   9.39,  1,     0),     \
   ("München",          48.08, 11.34,  1,      0),     \
   ("Münsingen",        46.53, 7.34,   1,      0),     \
   ("Münster",                    51.57,     7.37,    1,  0),  \
   ("Maastricht",       50.52, 5.43,   1,       0),    \
   ("Macao, China",               22.13,  113.36,   8,  0),    \
   ("Macon, Georgia",             32.50,   -83.38, -5,  0),    \
   ("Madison (Wis., US)", 43.05,  -89.22,  -6,  0),      \
   ("Madrid",           40.24, -3.41,    1,     0),    \
   ("Magdeburg",        52.07, 11.38,  1,       0),    \
   ("Mailand",          45.28, 9.12,     1,     0),    \
   ("Mainz",            50.01, 8.16,   1,       0),    \
   ("Malaga",           36.43, -4.25,    1,     0),    \
   ("Mallorca",         39.30, 3.00,     1,     0),    \
   ("Malmö",           55.36, 13.00,     1,     0),    \
   ("Managua, Nikaragva",         12.09,  -86.19,  -6,  0),    \
   ("Manaus",                     -2.53,  -60.07,  -4,  0),    \
   ("Manchester",       53.30, -2.15,  0,    0),       \
   ("Manchester, New Hampshire",  42.59,   -71.28, -5,   0),   \
   ("Manila",                     14.37,   121.00,  8,   0),   \
   ("Mannheim",         49.29, 8.29,   1,     0),      \
   ("Mantova",          45.09, 10.48,    1,   0),      \
   ("Maputo",                    -25.35,    32.21,  2,   0),   \
   ("Maracaibo, Venezuela",       10.31,  -71.58,  -4,   0),   \
   ("Marbella",         36.31, -4.53,    1,     0),    \
   ("Marburg",          50.49, 8.46,   1,       0),    \
   ("Marignane, France",          43.25,    5.13,     1,  0),  \
   ("Markkleeberg",               51.17,   12.23,     1,  0),  \
   ("Marseille",        43.18, 5.24,   1,      0),     \
   ("Marshall, TX",               32.33,   -94.23, -6,   0),   \
   ("Maseru",                    -29.11,    27.17,  2,   0),   \
   ("Mauritius",       -20.17,   57.33,  4,     0),    \
   ("Mbabane, Swasiland",        -26.04,   31.09,   2,  0),    \
   ("Mbale, Uganda",     1.04,   34.11,  3,  0),       \
   ("Medellin",       6.15,  -75.35,    -5,  0),       \
   ("Melbourne",      -37.49, 144.58,   10,  0),       \
   ("Melun, France",              48.32,    2.40,     1,  0),  \
   ("Memphis (Tenn., US)",35.08,  -90.03, -6,  0),    \
   ("Menton",           43.47,   7.30,  1,     0),     \
   ("Meran",            46.40, 11.09,    1,    0),     \
   ("Merlebach, France",          49.09,    6.48,     1,  0),  \
   ("Metz",             49.08,   6.10,  1,     0),     \
   ("Mexico City",     19.27, -99.16,    -6,   0),     \
   ("Miami Beach, FL",  25.47,  -80.08,  -5,   0),     \
   ("Miami, FL",        25.46,  -80.12,  -5,   0),     \
   ("Milwaukee (Wis., US)",43.02,  -87.55,  -6,   0),     \
   ("Minden",           52.17, 8.55,   1,      0),     \
   ("Minneapolis, Minnesota",44.59,  -93.13,  -6,    0),    \
   ("Minot, N. Dakota",           48.14,  -101.18, -7,  0),    \
   ("Minsk",            53.54,  27.34,  2,      0),    \
   ("Mississauga",                43.33,   -79.35, -5,  0),    \
   ("Mobile",           30.42,  -88.05,  -6,   0),     \
   ("Mâcon, Fr.",       46.18,   4.50,  1,     0),     \
   ("Modena",           44.40, 10.55,    1,    0),     \
   ("Mogadishu",                   2.01,    45.13,  3,   0),   \
   ("Moline, IL",                 41.31,   -90.31, -6,   0),   \
   ("Moncton",                    46.05,   -64.47, -4,   0),   \
   ("Monrovia",                    6.12,   -10.28,  0,   0),   \
   ("Mons",             50.27, 3.56,   1,        0),   \
   ("Monsey, NY",       41.07,  -74.04, -5,      0),   \
   ("Montauban, France",          44.01,    1.21,     1,  0),  \
   ("Montbeliard, France",        47.31,    6.48,     1,  0),  \
   ("Monte Carlo, Monaco",        43.44,    7.25,   1,    0),  \
   ("Monterrey, Mexico",          25.40, -109.19,  -6,    0),  \
   ("Montevideo",       -34.53, -56.11, -3,   0),      \
   ("Montgomery, AL",             32.23,   -86.19, -6,   0),   \
   ("Monticello",       41.39,  -74.42,  -5,    0),    \
   ("Montpelier, VT",             44.16,   -72.33, -5,   0),   \
   ("Montpellier",      43.36,   3.53,  1,    0),      \
   ("Montreal, Fr.",    47.32, 4.02,   1,     0),      \
   ("Montreal, Quebec, Can.", 45.31, -73.34,-5,  0),   \
   ("Moose Jaw",                  50.24,  -105.32, -6,  0),    \
   ("Moskau",           55.45, 37.35,  3,    0),       \
   ("Mukacevo, Ukraine",          48.27,   22.43,     2,  0),  \
   ("Muncie, Indiana",            40.11,   -85.23, -6,    0),  \
   ("N'Djamena",                  12.06,    14.35,  1,    0),  \
   ("Nîmes",            43.50,   4.21,  1,     0),     \
   ("Nürnberg",         49.27, 11.04,  1,      0),     \
   ("Nagold",           48.33, 8.43,   1,      0),     \
   ("Nairobi",           -1.17, 36.49,   3,    0),     \
   ("Nancy",            48.41,   6.12,  1,     0),     \
   ("Nandi, Simbabwe",           -20.59,   31.47,   2,   0),   \
   ("Nantes, France",             47.14,   -1.29,   1,   0),   \
   ("Naples (Fla., US)",26.08,  -81.48,  -5,     0),   \
   ("Nashville (Tenn., US)", 36.09, -86.48, -6,  0),   \
   ("Nassau, Germany",            50.19,    7.48,   1,   0),   \
   ("Natchez, Mississippi",       31.34,   -91.23, -6,   0),   \
   ("Neapel",           40.51, 14.17,    1,   0),      \
   ("Netanya",          32.20, 34.51,  2,     0),      \
   ("Neu Dehli (GMT+5)", 28.18, 77.28,     5,    0),     \
   ("Neu Dehli (GMT+6)", 28.18, 77.28,     6,    0),     \
   ("Neu Fahrland",               52.27,    13.03,    1,  0),   \
   ("Neumünster",       54.04, 9.59,   1,      0),     \
   ("Neuruppin",        52.55, 12.48,  1,      0),     \
   ("Neustadt/Weinstraße", 49.21, 8.08,   1,   0),        \
   ("Neustrelitz",      53.21, 13.04,  1,      0),     \
   ("New Bedfort, MA",  41.38,  -70.56, -5,    0),     \
   ("New Brunswick",    40.29,  -74.27,  -5,   0),     \
   ("New Haven (Conn., US)", 41.18, -72.56, -5,  0),   \
   ("New Orleans, Louisiana",29.58,  -90.07,  -6,   0),   \
   ("New York, Brooklyn",40.42,  -74.00,  -5,    0),    \
   ("New York, NY",     40.43,  -74.01,  -5,     0),   \
   ("Newark (N.J., US)",40.44,  -74.10,  -5,     0),   \
   ("Newcastle",        54.12,  -5.45,  0,       0),   \
   ("Newport (R.I., US)", 41.13, -71.18, -5,     0),   \
   ("Niagra Falls, NY",           43.06,   -79.03, -5,   0),   \
   ("Niamey",                     13.19,     2.03,  1,    0),  \
   ("Nice",             43.42, 7.15,   1,     0),      \
   ("Nicosia, Cyprus",  34.47,   33.29,  2,   0),      \
   ("Nikolayev, Ukraine",         49.31,   23.58,     2,   0), \
   ("Nizhniy Novgorod",           56.20,   44.10,   4,   0),   \
   ("Nizza Monferrato", 44.46,   8.21,  1,      0),    \
   ("Nome, AK",                   64.30,  -165.25, -10,  0),   \
   ("Nordhausen", 51.30,    10.47,  1,  0),  \
   ("Norfolk, Virginia",          36.51,   -76.17, -5,   0),   \
   ("North Bay",                  46.19,   -79.28, -5,   0),   \
   ("Norwich",          52.38,   1.18,  0,     0),     \
   ("Nottingham",       52.58,  -1.10,  0,     0),     \
   ("Nouakchott",                 18.05,   -15.35,  0,   0),   \
   ("Noumea, New Caledonia",     -22.07,  166.30,  11,   0),   \
   ("Novi Sad",        45.15, 19.50,     1,   0),      \
   ("Nowgorod",         58.35,   31.14,  3,   0),      \
   ("Oakland, CA",                37.48,  -122.16, -8,   0),   \
   ("Oberkirch",                  48.31,    8.05,     1,  0),  \
   ("Obernai, France",            48.28,    7.29,     1,   0), \
   ("Odense, Denmark",            55.26,  -10.18,   1,   0),   \
   ("Oderberg",                   52.52,   14.02,     1,  0),  \
   ("Odessa",           46.28, 30.44,  3,     0),      \
   ("Offenbach",        50.08, 8.47,   1,     0),      \
   ("Offenburg",                  48.28,    7.57,     1,  0),  \
   ("Ogden, Utah",                41.14,  -111.58, -7,    0),  \
   ("Oklahoma City",              35.28,   -97.31, -6,    0),  \
   ("Oldenburg in Holstein",54.17, 10.52, 1,    0),       \
   ("Oldenburg",        53.08, 8.13,   1,       0),    \
   ("Olomouc",         49.36, 17.16,     1,     0),    \
   ("Omaha, Nebraska",  41.16,  -95.57,  -6,    0),    \
   ("Omsk",             54.57,   73.21,  6,     0),    \
   ("Oradea",          47.03, 21.57,     2,     0),    \
   ("Oranienburg",                52.45,   13.14,     1,  0),  \
   ("Orlando, FL",      28.32,  -81.23,  -5, 0),       \
   ("Orléans, Fr.",     47.55,   1.54,  1,   0),       \
   ("Osaka, Japan",               34.45,  135.28,   9,   0),   \
   ("Oshawa",                     43.54,   -78.52, -5,   0),   \
   ("Oslo",            59.55, 10.45,     1,    0),     \
   ("Osnabrück",        52.16, 8.02,   1,      0),     \
   ("Ostende",          51.13, 2.55,   1,      0),     \
   ("Ostrava",         49.50, 18.17,     1,    0),     \
   ("Ottawa",         45.25, -75.72,    -5,    0),     \
   ("Ouagadougou",                12.12,    -1.24,  0,  0),    \
   ("Oxford",           51.46,  -1.15,  0,     0),     \
   ("Paderborn",        51.43, 8.45,   1,      0),     \
   ("Padova",           45.25, 11.53,    1,    0),     \
   ("Paducah, KY",                37.05,   -88.36, -5,  0),    \
   ("Panama, Panama",    8.58,  -79.31, -5,    0),     \
   ("Paramaribo, Surinam",         5.46,  -55.15,  -3,   0),   \
   ("Parchim",          53.25,  11.51,  1,     0),     \
   ("Paris",            48.52, 2.20,   1,      0),     \
   ("Parma",            44.48, 10.20,    1,    0),     \
   ("Pasadena, CA",               34.09,  -118.09, -8,   0),   \
   ("Paterson, NJ",               40.55,   -74.10, -5,   0),   \
   ("Pau, France",                43.18,   -0.22,     1,  0),  \
   ("Pazardjik",       42.12, 24.20,     2,    0),     \
   ("Peking (Beijing)",39.55, 116.25,    8,    0),    \
   ("Pensacola, FL",              30.25,   -87.13, -5,   0),   \
   ("Peoria, IL",       40.42,  -89.36, -6,   0),      \
   ("Perigueux, France",          45.11,    0.43,     1,  0),  \
   ("Perleberg",        53.04, 11.51,  1,      0),     \
   ("Perm",             57.55,   56.03,  5,    0),     \
   ("Perpignan",        42.41,   2.53,  1,     0),     \
   ("Perth",                     -31.50,   116.10,  8,   0),   \
   ("Perugia",          43.08, 12.22,    1,    0),     \
   ("Peterborough",               44.19,   -78.19, -5,   0),   \
   ("Pforzheim",        48.54, 8.42,   1,      263),     \
   ("Phalsbourg, France",         48.46,    7.16,     1,  0),  \
   ("Philadelphia, Pennsylvania",39.57,  -75.07,  -5,  0), \
   ("Phnom Penh, Kambodscha",     11.32,  104.47,   7,   0),   \
   ("Phoenix, Arizona", 33.27, -112.05,  -7,  0),      \
   ("Piatra Neamt",    46.56, 26.22,     2,   0),      \
   ("Pierre, South Dakota",       44.22,  -100.21, -6,   0),   \
   ("Piestany",        48.36, 17.50,     1,     0),    \
   ("Pilsen",          49.45, 13.23,     1,     0),    \
   ("Pisa",             43.43, 10.23,    1,     0),    \
   ("Pittsburgh, Pennsylvania",40.26,  -80.00,  -5,  0),  \
   ("Pittsfield, MA",             42.27,   -73.15, -5,   0),   \
   ("Pjongjang (P´yongyang)",39.01, 125.45, 9,   0),      \
   ("Plano, TX",        33.02,  -96.42, -6,    0),     \
   ("Plovdiv",         42.09, 24.45,     2,    0),     \
   ("Plymouth",         50.23,  -4.10,  0,     0),     \
   ("Pocatello, Idaho",           42.52,  -112.27, -7,   0),   \
   ("Poitiers, France",           46.35,    0.20,     1,  0),  \
   ("Port Arthur, TX",            29.53,   -93.56, -6,  0),    \
   ("Port Au Prince, Haiti",      18.34,  -72.21,  -5,  0),    \
   ("Port Louis, Mauritius",     -20.09,   57.30,   4,  0),    \
   ("Port Moresby, Papua-Neuguinea",-9.26,  147.00,  10,   0),   \
   ("Port Said, Egypt",           30.54,   32.05,   2,   0),   \
   ("Portland (Maine, US)", 43.39, -70.17, -5,  0),    \
   ("Portland (Oreg, US)", 45.33, -112.36, -8,  0),    \
   ("Porto Novo",                  6.18,     2.28,  1,   0),   \
   ("Porto",            41.11, -8.36,    0,    0),     \
   ("Portsmouth",       50.48,  -1.05,  0,     0),     \
   ("Portsmouth, New Hampshire",  43.04,   -70.45, -5,   0),   \
   ("Portsmouth, Virginia",       36.50,   -76.17, -5,   0),   \
   ("Potsdam",          52.24, 13.04,  1,      0),     \
   ("Prag",            50.05, 14.26,     1,    0),     \
   ("Presov",          49.00, 21.15,     1,    0),     \
   ("Pretoria, South Africa",    -25.38,   28.20,   2,  0),    \
   ("Prince Rupert, British Columbia",54.19,-130.19, -8,   0),   \
   ("Pritzwalk",        53.09, 12.10,  1,      0),     \
   ("Providence, RI",   41.50,  -71.25,  -5,   0),     \
   ("Provo, Utah",                40.14,  -111.39, -7,   0),   \
   ("Pueblo",                     38.16,  -104.37, -7,   0),   \
   ("Puta, Aserbaidschan",        40.18,   49.41,   4,   0),   \
   ("Quebec",         46.49, -71.14,    -5,     0),    \
   ("Quito",                      -0.17,   -78.32, -5,  0),    \
   ("Röbel",   53.22,    12.36, 1,  0),  \
   ("Raananna, Israel", 32.11,   35.52,  2,      0),   \
   ("Rabat",                      34.01,    -6.31,  1,   0),   \
   ("Rachki, Ukraine",            49.30,   29.54,     2,  0),  \
   ("Racine (Wis., US)",          42.44,   -87.47, -6,   0),   \
   ("Radauti",         47.51, 25.55,     2,     0),    \
   ("Raleigh, NC",      35.47,  -78.39, -5,     0),    \
   ("Ramat Gan, Israel",32.05,   34.49,  2,     0),    \
   ("Ramsgate",         51.20,   1.25,  0,      0),    \
   ("Rangun (GMT+6)",    16.47, 96.10,   6,     0),    \
   ("Rangun (GMT+7)",    16.47, 96.10,   7,     0),    \
   ("Rapid City, South Dakota",   44.05,  -103.13, -6,  0),    \
   ("Rathenow",         52.36, 12.20,  1,    0),       \
   ("Reading",          51.28,  -0.59,  0,   0),       \
   ("Reading, Pennsylvania",      40.20,   -75.56, -5,  0),    \
   ("Recklinghausen",   51.36, 7.13,   1,      0),     \
   ("Redmond, WA",      47.24, -122.04, -8,    0),     \
   ("Regensburg",       49.01, 12.06,  1,      0),     \
   ("Regina",                     50.27,  -104.37, -6,   0),   \
   ("Rehovot",          31.54,  34.49,  2,     0),     \
   ("Reims",            49.15,   4.02,  1,     0),     \
   ("Reims, France",              49.15,    4.02,     1,  0),  \
   ("Rennes, France",             48.05,   -1.41,     1,  0),  \
   ("Reno, NV",                   39.31,  -119.49, -8,  0),    \
   ("Reykjavik",                  64.09,   -21.39,  0,  0),    \
   ("Rhodos",           36.10, 28.00,    2,   0),      \
   ("Richmond, Virginia",         37.32,   -77.26, -5,   0),   \
   ("Riga",             56.57,  24.06,  2,     0),     \
   ("Rijeka",          45.20, 14.27,     1,    0),     \
   ("Rinteln",          52.11, 9.04,   1,      0),     \
   ("Rio de Janeiro",   -22.54, -43.15, -3,    0),     \
   ("Roanne, France",             46.02,    4.04,     1,   0), \
   ("Roanooke, Virginia",         37.16,   -79.57, -5,  0),    \
   ("Rochester",        51.24,   0.30,  0,     0),     \
   ("Rochester, Minnesota",       44.01,   -92.28, -6,  0),    \
   ("Rochester, NY",              43.10,   -77.36, -5,  0),    \
   ("Rockford, IL",               42.16,   -89.06, -6,  0),    \
   ("Rom",              41.54, 12.29,    1,    0),     \
   ("Rostock",          54.05, 12.07,  1,      0),     \
   ("Rothenburg an der Oder",52.01, 15.25, 1,  0),        \
   ("Rothenburg ob der Tauber",49.23,10.10,1,  0),        \
   ("Rothenburg",       51.20,   14.58, 1,     0),     \
   ("Rotterdam",        51.55, 4.28,   1,      0),     \
   ("Rouen",            49.26,   1.05,  1,     0),     \
   ("Ruse",            43.50, 25.57,     2,    0),     \
   ("Rust, Germany",              48.16,    7.43,     1,  0),  \
   ("Saarbrücken",      49.14, 6.59,   1,      0),     \
   ("Sacramento, CA",   38.35, -121.30, -8,    0),     \
   ("Safad, Israel",    32.58,   35.30,  2,    0),     \
   ("Saginaw, MI",                43.26,   -83.56, -5,  0),    \
   ("Saint-Avold, France",        49.06,    6.42,     1,  0),  \
   ("Saint-Die, France",          48.17,    6.57,     1,  0),  \
   ("Saint-Etienne, France",      45.26,    4.24,     1,  0),  \
   ("Saint-Fons, France",         45.42,    4.52,     1,  0),  \
   ("Saint-Laurent-du-Var, France (1)",45.23,5.44,    1,  0),  \
   ("Saint-Laurent-du-Var, France (2)",43.40,7.11,    1,  0),  \
   ("Saint-Louis, Fr.", 47.35,   7.34,  1,     0),     \
   ("Saint-Quentin, France",      49.51,    3.17,     1,  0),  \
   ("Saint Anne's",     53.45,  -3.02,  0,     0),     \
   ("Salem (Oreg, US)",           44.56,  -123.02, -8,  0),    \
   ("Salina (Kans., US)",         38.51,   -97.37, -6,  0),    \
   ("Saloniki",         40.39, 23.01,    2,   0),      \
   ("Salt Lake City, Utah",40.46, -111.53,  -7,    0),    \
   ("Salzburg",         47.48, 13.02,  1,     0),      \
   ("Salzgitter",       52.10, 10.25,  1,     0),      \
   ("San Angelo, TX",             31.28,  -100.26, -6,  0),    \
   ("San Antonio, TX",  29.28,  -98.31,  -6,    0),    \
   ("San Bernardino, CA",         34.07,  -117.28, -8,  0),    \
   ("San Diego",        32.43, -117.09,  -8,   0),     \
   ("San Francisco",    37.48, -122.24,  -8,   0),     \
   ("San Jose, CA",               37.20,  -121.53, -8,   0),   \
   ("San Juan (P.R.)",  18.28, -66.07, -4,     0),     \
   ("San Salvador, El Salvador",  13.59,  -89.11,  -6,   0),   \
   ("Sana, Jemen",      15.11,   44.01,  3,    0),     \
   ("Sankt Gallen",     47.25, 9.23,   1,      0),     \
   ("Santa Barbara, CA",          34.25,  -119.42, -8,   0),   \
   ("Santa Cruz, CA",             36.58,  -122.01, -8,   0),   \
   ("Santa Fe (N.Mex., US)", 35.42, -106.57, -7,  0),  \
   ("Santa Fe, NM",               35.41,  -105.56, -7,   0),   \
   ("Santiago de Chile", -33.27, -70.40, -4,    0),    \
   ("Santo Domingo, Dominican Republic",18.30,-69.56,-4,  0),    \
   ("Sao Paulo",       -23.32, -46.37,   -3,    0),    \
   ("Sarajevo",        43.52, 18.25,     1,     0),    \
   ("Sarasota, FL",               27.20,   -82.33, -5,   0),   \
   ("Sarrebourg, France",         48.44,    7.03,     1,  0),  \
   ("Sarreguemines, France",      49.06,    7.03,     1,  0),  \
   ("Saskatoon",                  52.08,  -106.40, -6,    0),  \
   ("Satu Mare",       47.48, 22.53,     2,    0),     \
   ("Sault St Marie",             46.30,   -84.20, -5,   0),   \
   ("Savannah, Georgia",          32.05,   -81.06, -5,   0),   \
   ("Saverne, France",            48.44,    7.22,     1,  0),  \
   ("Scarsdale, NY",    40.59,  -73.49, -5,    0),     \
   ("Schenectady, NY",            42.49,   -73.56, -5,   0),   \
   ("Schwedt/Oder",               53.03,   14.17,     1,  0),  \
   ("Schwerin",         53.38, 11.25,  1,      0),     \
   ("Scranton, Pennsylvania",     41.25,   -75.40, -5,  0),    \
   ("Seattle, WA",      47.36, -122.20,  -8,    0),    \
   ("Sedan, France",              49.42,    4.57,     1,  0),  \
   ("Selestat, France",           48.16,    7.27,     1,  0),  \
   ("Sens",             48.12,   3.17,  1,     0),     \
   ("Seoul (Soul)",    37.33, 126.58,    9,    0),     \
   ("Sevilla",          37.23, -5.59,    1,    0),     \
   ("Shanghai",        31.14, 121.28,    8,    0),     \
   ("Sheboygan (Wis., US)",       43.45,   -87.43, -6,  0),    \
   ("Shechem, Israel",  32.13,   35.15,  2,    0),     \
   ("Sheffield",        53.23, -1.30,  0,      0),     \
   ("Shenyang",        41.48, 123.27,    8,    0),     \
   ("Sherbrooke",                 45.24,   -71.51, -5,   0),   \
   ("Sheridan, Wyoming",          44.48,  -106.57, -7,   0),   \
   ("Shkoder, Albania", 42.05,   19.30,  1,    0),     \
   ("Shreveport, Louisiana",      32.31,   -93.45, -6,   0),   \
   ("Siena",            43.19, 11.21,    1,   0),      \
   ("Sighetul Marmatiei", 47.56, 23.54,     2,     0),    \
   ("Silver Spring",    39.02,  -77.03,  -5,    0),    \
   ("Simferopol, Ukraine",        44.57,   34.06,     2,  0),  \
   ("Singapur",        11.22, 103.48,    8,     0),    \
   ("Sioux City, IA",             42.30,   -96.25, -6,   0),   \
   ("Sioux Falls, South Dakota",  43.33,   -96.44, -6,   0),   \
   ("Siyäzän, Aserbaidschan",     41.04,   49.06,   4,   0),   \
   ("Skokie, IL",       42.02,  -87.46, -6,     0),    \
   ("Skopje",          41.59, 21.26,     1,     0),    \
   ("Slavuta, Ukraine",           50.18,   26.52,     2,  0),  \
   ("Sobernheim",       49.47, 7.38,   1,     0),      \
   ("Sofia",           42.41, 23.19,     2,   0),      \
   ("Solihull",         52.25,  -1.45,  0,    0),      \
   ("Somerville, MA",             42.23,   -71.06, -5,   0),   \
   ("Sopron",          47.41, 16.36,     1,    0),     \
   ("South Bend, Indiana",        41.41,   -86.15, -6,   0),   \
   ("Southend-on-SEA",  51.33,   0.43,  0,      0),    \
   ("Southport",        53.39,  -3.01,  0,      0),    \
   ("Spartanburg, SC",            34.57,   -81.56, -5,   0),   \
   ("Spiazzo",          46.07, 10.40,    1,     0),    \
   ("Split",           43.31, 16.27,     1,     0),    \
   ("Spokane, WA",                47.40,  -117.26, -8,  0),    \
   ("Springfield (Mass., US)",42.07,  -72.36,  -5, 0),    \
   ("Springfield, IL",            39.48,   -89.39, -6,   0),   \
   ("Springfield, Missouri",      37.13,   -93.18, -6,   0),   \
   ("Springfield, OH",            39.57,   -83.48, -5,   0),   \
   ("St Catherines",              43.10,   -79.15, -5,   0),   \
   ("St John's",                  47.34,   -52.43, -4,   0),   \
   ("St John",                    45.16,   -66.04, -4,   0),   \
   ("St. Cloud, Minnesota",       45.34,   -94.10, -6,   0),   \
   ("St. Joseph, Missouri",       39.46,   -94.51, -6,   0),   \
   ("St. Louis",        38.38,  -90.11,  -6,    0),    \
   ("St. Louis, Missouri",        38.38,   -90.12, -6,    0),  \
   ("St. Paul, Minnesota",        44.57,   -93.06, -6,    0),  \
   ("St. Petersburg",   59.55, 30.15,  3,      0),     \
   ("St. Petersburg, FL",         27.47,   -82.38, -5,   0),   \
   ("Stamford, CA",     41.03,  -73.33,  -5,   0),     \
   ("Stendal",          52.36, 11.51,  1,      0),     \
   ("Stockholm",       59.20, 18.03,     1,    0),     \
   ("Stockton, CA",               37.58,  -121.17, -8,  0),    \
   ("Strasbourg",       48.35,   7.45,  1,     0),     \
   ("Straubing",        48.53, 12.34,  1,      0),     \
   ("Strausberg",       52.35, 13.53,  1,      0),     \
   ("Stuebenville, OH",           40.22,   -80.37, -5,  0),    \
   ("Stuttgart",        48.46, 9.11,   1,      0),     \
   ("Subotica",        46.06, 19.39,     1,    0),     \
   ("Suceava",         47.39, 26.19,     2,    0),     \
   ("Sudbury",                    46.29,   -80.59, -5,  0),    \
   ("Suez, Egypt",                29.58,   32.33,   2,  0),    \
   ("Suhl",             50.37,  10.41,  1,     0),     \
   ("Sumqayit, Aserbaidschan",    40.36,   49.45,   4,  0),    \
   ("Sunderland",       54.45,  -1.23,  0,      0),    \
   ("Superior (Wis., US)",        46.43,   -92.06, -6,  0),    \
   ("Sydney",         -33.52, 151.13,   10,     0),    \
   ("Sydney, Canada",             46.08,   -60.12, -4,  0),    \
   ("Syracuse, NY",               43.03,   -76.09, -5,  0),    \
   ("Szeged, Hungary",            46.19,   20.05,   1,  0),    \
   ("Tübingen",         48.31, 9.02,   1,    0),       \
   ("Tacoma, WA",                 47.15,  -122.26, -8,  0),    \
   ("Tahiti, Polynesia",         -18.18, -149.26, -10,  0),    \
   ("Taipei",            25.03, 121.30,  8,    0),     \
   ("Tallahassee, FL",            30.27,   -84.27, -5,  0),    \
   ("Tallinn",          59.25,  24.45,  2,      0),    \
   ("Tampa, FL",        27.57,  -82.27,  -5,    0),    \
   ("Taraclia, Moldova",          45.54,   28.41,   2,  0),    \
   ("Tarbes, France",             43.14,    0.05,     1,   0), \
   ("Tarnów",           52.47, 14.58,  1,     0),      \
   ("Taschkent",        41.20, 69.18,  6,     0),      \
   ("Tblisi",           41.43, 44.49,  3,     0),      \
   ("Teaneck, NJ",      40.53,  -74.01, -5,   0),      \
   ("Tegucigalpa, Honduras",      14.17,  -87.24,  -6,   0),   \
   ("Teheran (GMT+3)", 35.40, 51.26,     3,     0),    \
   ("Teheran (GMT+4)", 35.40, 51.26,     4,     0),    \
   ("Tel Aviv",         32.04, 34.46,  2,       0),    \
   ("Tenerife, Spain",  28.02,   16.34,  1,     0),    \
   ("Teplice",         50.39, 13.48,     1,     0),    \
   ("Terre Houte, Indiana",       39.28,   -87.24, -6,  0),    \
   ("Teverya, Israel",  32.47,   35.32,  2,    0),     \
   ("Texarkana, TX",              33.26,   -94.03, -6,   0),   \
   ("Thessaloniki, Greece",       40.38,   22.58,   2,   0),   \
   ("Thessalonikia, Greece",      40.39,   23.01,   2,   0),   \
   ("Thimbu, Bhutan",             27.28,   89.38,   6,   0),   \
   ("Thionville, France",         49.22,    6.10,     1, 0),   \
   ("Thunder Bay",                48.23,   -89.15, -5,   0),   \
   ("Tiberias, Israel",           32.47,   35.30,   2,   0),   \
   ("Tijuana, Mexico",            32.30, -117.02,  -6,   0),   \
   ("Tilburg",          51.34, 5.05,   1,      0),     \
   ("Timisoara",       45.45, 21.13,     2,    0),     \
   ("Tinton Falls, NJ",           40.17,   -74.06,    -5,  0), \
   ("Tirana, Albania",            41.21,   19.49,   1,   0),   \
   ("Tirana, Albania",  41.20,   19.50,  1,   0),      \
   ("Tirgu Mures",     46.33, 24.33,     2,   0),      \
   ("Tokyo",           35.42, 139.46,    9,    0),     \
   ("Toledo, OH",                 41.39,   -83.33, -5,  0),    \
   ("Topeka (KS, US)",  39.03,  -95.41,  -6,    0),    \
   ("Toronto",        43.39, -79.23,    -5,     0),    \
   ("Torremolinos",     36.37, -4.30,    1,     0),    \
   ("Toul, France",               48.41,    5.54,     1,  0),  \
   ("Toulon",           43.07,   5.56,  1,    0),      \
   ("Toulon, France",             43.07,    5.56,     1,  0),  \
   ("Toulouse",         43.36,   1.26,  1,    0),      \
   ("Tours",            47.23,   0.41,  1,    0),      \
   ("Towson, MD", 39.17,  -76.37,  -5,   0),   \
   ("Tralee",           52.16, -9.42,  0,     0),      \
   ("Trenton, NJ",                40.13,   -74.48, -5,  0),    \
   ("Trier",            49.45, 6.38,   1,    0),       \
   ("Trieste",          45.40, 13.46,    1,  0),       \
   ("Trikala",          39.34, 21.46,    2,  0),       \
   ("Tripoli",                    32.50,    13.13,  1,   0),   \
   ("Trnava",          48.23, 17.35,     1,    0),     \
   ("Trois Riveres",              46.21,   -72.33, -5,  0),    \
   ("Trondheim",       63.25, 10.25,     1,      0),   \
   ("Troy, NY",                   42.44,   -73.41, -5,  0),    \
   ("Troyes",           48.18,   4.05,  1,    0),      \
   ("Tucson",           32.13, -110.58,  -7,  0),      \
   ("Tulsa, Oklahoma",            36.09,   -96.00, -6,  0),    \
   ("Tunis",                      36.30,    10.08,  1,  0),    \
   ("Turin",            45.04, 7.40,     1,     0),    \
   ("Turku",           60.27, 22.17,     2,     0),    \
   ("Ulan Bator, Mongolia",       47.27,  106.24,   8,   0),   \
   ("Urbana, IL",                 40.07,   -88.12, -6,    0),  \
   ("Usti nad Labem",  50.40, 14.02,     1,    0),     \
   ("Utica, NY",                  43.06,   -75.14, -5,  0),    \
   ("Utrecht",          52.05, 5.08,   1,      0),     \
   ("Vaduz, Liechtenstein",       47.08,    9.32,   1,   0),   \
   ("Valence, France",            44.56,    4.54,     1,  0),  \
   ("Valencia",         39.28, -0.22,    1,   0),      \
   ("Valenciennes, France",       50.21,    3.32,     1,  0),  \
   ("Vancouver",      49.16, -123.07,   -8,     0),    \
   ("Venedig",          45.27, 12.21,    1,     0),    \
   ("Venissieux, France",         54.41,    4.53,     1,  0),  \
   ("Verdun, France",             49.10,    5.23,     1,  0),  \
   ("Verl",  51.53,   8.31,   1,  0),  \
   ("Verona",           45.27, 11.00,    1,    0),     \
   ("Versailles, Fr.",  48.48,   2.08,  1,     0),     \
   ("Vevey",            46.28, 6.51,   1,      0),     \
   ("Vichy, France",              46.08,    3.26,     1,  0),  \
   ("Victoria, British Columbia",   48.26,  -123.22, -8,  0),    \
   ("Victoria, Hongkong",         22.10,   114.18,  8,   0),   \
   ("Vientiane, Laos",            17.53,  102.38,   7,   0),   \
   ("Vilnius",          54.41,  25.19,  2,      0),    \
   ("Vista Alegre, Spain (37,54 N, 4,09 W)", 37.54, -4.09, 1,  0), \
   ("Vista Alegre, Spain (38,18 N, 3,04 W)", 38.18, -3.04, 1,  0), \
   ("Vittel",           48.12,   5.57,  1,    0),      \
   ("Volos",            39.21, 22.56,    2,   0),      \
   ("W. Palm Beach, FL",          26.43,   -80.03, -5,  0),    \
   ("Wörlitz",          51.50, 12.25,  1,      0),     \
   ("Würzburg",         49.48, 9.56,   1,      0),     \
   ("Waco, TX",                   31.33,   -97.08, -6,   0),   \
   ("Waldkirch",                  48.05,    7.57,     1, 0),   \
   ("Walla Walla, WA",            46.04,  -118.20, -8,   0),   \
   ("Warendorf",                  51.57,     7.59,    1, 0),   \
   ("Warschau",         52.15, 21.00,  1,     0),      \
   ("Washington, DC",   38.54,  -77.01,  -5,  0),      \
   ("Wasselonne",       48.38,   7.27,  1,    0),      \
   ("Waterloo, IA",               42.30,   -92.20, -6,  0),    \
   ("Watford",          51.40,  -0.25,  0,     0),     \
   ("Weiden in der Oberpfalz",49.41,12.10,1,    0),       \
   ("Wellington, New Zealand",   -41.18,  174.59,  12,   0),   \
   ("Wheeling, West Virginia",    40.04,   -80.43, -5,   0),   \
   ("White Plains, NY",           41.02,   -73.46, -5,   0),   \
   ("Whitehorse",                 60.43,  -135.03, -8,   0),   \
   ("Wichita (Kans., US)",        37.42,   -97.20, -6,   0),   \
   ("Wichita, TX",      37.41,  -97.20,  -6,    0),    \
   ("Wien",             48.13, 16.20,  1,       0),    \
   ("Wiesbaden",        50.05, 8.14,   1,       0),    \
   ("WilkesEBarre, Pennsylvania", 41.15,   -75.53, -5,    0),  \
   ("Wilmington, Delaware",       39.45,   -75.33, -5,    0),  \
   ("Wilmington, NC",             34.14,   -77.57, -5,    0),  \
   ("Windhoek",                  -22.20,    17.04,  2,    0),  \
   ("Windsor",                    42.19,   -83.02, -5,    0),  \
   ("Winnipeg",       49.53, -97.09,    -6,    0),     \
   ("Winston Salem, NC",          36.06,   -80.15, -5,   0),   \
   ("Winterthur",       47.30, 8.43,   1,      0),     \
   ("Wismar",           53.53, 11.28,  1,      0),     \
   ("Wittenberg",       51.52, 12.39,  1,      0),     \
   ("Wittenberge",      53.00, 11.44,  1,      0),     \
   ("Wittstock",        53.10, 12.29,  1,      0),     \
   ("Woodbourne",       41.46,  -74.35, -5,    0),     \
   ("Worcester, MA",              42.16,   -71.48, -5,  0),    \
   ("Worms",            49.38,   8.22,  1,    0),      \
   ("Woronesch, Russia",51.42,   39.15,  3,   0),      \
   ("Wroczlaw (Breslau)", 51.06, 17.00,  1,   0),        \
   ("Wuppertal",        51.16, 7.11,   1,     0),      \
   ("Yakima, WA",                 46.36,  -120.31, -8,  0),    \
   ("Yaounde",                     3.31,    11.19,  1,  0),    \
   ("Yellowknife",                62.27,  -114.23, -7,  0),    \
   ("Yellowstone Lake", 44.25, -110.22,  -7,    0),    \
   ("Yerevan, Armenia",           39.56,   44.45,   4,  0),    \
   ("Yonkers, NY",                40.56,   -73.54, -5,  0),    \
   ("York, Pennsylvania",         39.58,   -76.44, -5,  0),    \
   ("Youngstown, OH",             41.06,   -80.39, -5,  0),    \
   ("Yuma, Arizona",              32.43,  -114.37, -7,  0),    \
   ("Zürich",           47.23, 8.32,   1,     0),      \
   ("Zagreb",          45.48, 15.58,     1,   0),      \
   ("Zanesville, OH",             39.56,   -82.31, -5,   0),   \
   ("Zefat, Israel",              32.57,   35.30,   2,   0),   \
   ("Zhitomir, Ukraine",          50.15,   28.40,     2, 0),   \
   ("Zilina",                     49.14,   18.46,     1, 0),   \
   ("Zug",              47.10, 8.31,   1,     0),      \
   ("Zwolle",           52.30, 6.05,   1,     0)      \
]

# Returns a list of names with locations (which can be passed
# as a parameter for getLocationData) and which can be presented
# to the user in a Select Location dialog box
def getLocationList():
  namesLocations = []
  for i in range(len(builtinLocations)):
    namesLocations.append(builtinLocations[i][0])
  return namesLocations

# Returns a tuple (latitude, longitude, timezone, elevation) of the
# location locationName, or None if the location was not found.
def getLocationData(locationName):
  for i in range(len(builtinLocations)):
    if(builtinLocations[i][0] == locationName):
      result = (builtinLocations[i][1] * 100, builtinLocations[i][2] * 100, builtinLocations[i][3], builtinLocations[i][4])
      return result
  return None
