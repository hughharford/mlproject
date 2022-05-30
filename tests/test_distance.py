from mlproject import haversine

def test_haversine():
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 51.43651769861451, -0.05654153662997176 #12 dhc
    distance = haversine(lon1, lat1, lon2, lat2)
    
    assert distance == 70.00789153218594
