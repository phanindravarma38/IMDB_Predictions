# -*- coding: utf-8 -*-
"""
Created on  Thur Nov 16 1 09:12:28 2016

@author: Phanindra Varma Sagiraju
"""

if movie['content_rating'] is None or len(movie['content_rating']) == 0:
        parsed_movie['week_day'] = "No_Date"
else:
    if len(movie['content_rating']) == 18:
            x = movie['content_rating'][15].strip()
            if len(x) > 0:
                try:
                    k = x.split(" ")
                    if len(k) == 4:
                        k = " ".join(k[0:3])
                        d = datetime.strptime(k, '%d %B %Y')
                        parsed_movie['week_day'] = d.weekday()
                        parsed_movie['date'] = d
                        parsed_movie['season'] = get_season(d.timetuple().tm_yday)
                except:
                    parsed_movie['week_day'] = x
                    parsed_movie['date'] = "Exception_18"
            
    elif len(movie['content_rating']) == 16:
            y = movie['content_rating'][13].strip()
            if len(y) > 0:
                try:
                    k1 = y.split(" ")
                    if len(k1) == 4:
                        k1 = " ".join(k1[0:3])
                        d1 = datetime.strptime(k1, '%d %B %Y')
                        parsed_movie['week_day'] = d1.weekday()
                        parsed_movie['date'] = d1
                        parsed_movie['season'] = get_season(d1.timetuple().tm_yday)
                except:
                    parsed_movie['week_day'] = y
                    parsed_movie['date'] = "Exception_19"
            
    elif len(movie['content_rating']) == 14:
           y = movie['content_rating'][11].strip()
           if len(y) > 0:
                try:
                    k1 = y.split(" ")
                    if len(k1) == 4:
                        k1 = " ".join(k1[0:3])
                        d1 = datetime.strptime(k1, '%d %B %Y')
                        parsed_movie['week_day'] = d1.weekday()
                        parsed_movie['date'] = d1
                        parsed_movie['season'] = get_season(d1.timetuple().tm_yday)
                except:
                    parsed_movie['week_day'] = y
                    parsed_movie['date'] = "Exception_19"
            
        else:
            parsed_movie['week_day'] = "Series_No_Date"#movie['week_day']

To fetch the seasons, the logic used is

spring = range(80, 172)
summer = range(172, 264)
fall = range(264, 355)

def get_season(doy):
    # "day of year" ranges for the northern hemisphere
    # winter = everything else
    if doy in spring:
      season = 'spring'
    elif doy in summer:
      season = 'summer'
    elif doy in fall:
      season = 'fall'
    else:
      season = 'winter'
    return season
