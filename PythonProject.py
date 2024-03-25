import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

plt.xkcd()

# PageViews Dataset

file = r'C:\Users\MY LAPTOP\Downloads\pageviews-20190615-200000.txt'
hedars = ['Analytics', 'Data Lake', 'Traffic', 'Pageviews']
page_views = pd.read_csv(file, header=None, index_col=False, names=hedars, delimiter=' ', low_memory=False)

# plot 1
'''
This plot describes a line plot that has the count of each wikimedia for a specific language in June, 15th in 2019.
I divided the four languages, each one in an independent dataframe and then concatenated them in one dataframe.
'''
plt.style.use('seaborn')
es = page_views[page_views.Analytics == 'es']
fr = page_views[page_views.Analytics == 'fr']
cs = page_views[page_views.Analytics == 'cs']
ru = page_views[page_views.Analytics == 'ru']

p = pd.concat([es, fr, cs, ru], ignore_index=True)
sb.lmplot(x='Traffic', y='Traffic', col="Analytics", hue="Analytics", data=p, col_wrap=2, ci=None, height=6,
          scatter_kws={"s": 100}, line_kws={"lw": 1}).fig.suptitle('enwiki VS eswili for the four most used '
                                                                   'languages in June, 15th in 2019')
plt.legend()
plt.show()

# plot 2
'''
This plot describes a pie chart plot showing the difference between english wikimedia and spanish wikimedia.
I took the size of each wikimedia language then i drew the pie chart.
'''
es_m = len(page_views[page_views.Analytics == 'es.m'])
en_m = len(page_views[page_views.Analytics == 'en.m'])
sb.set_theme()
data = [es_m, en_m]
labels = ['es_wikimedia', 'en_wikimedia']
colors = ['#b00149', '#0a481e']
explode = [0, 0.1]

plt.pie(data, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90, shadow=True, colors=colors)
plt.title('Count of wikimedia between Spanish wikimedia and English wikimedia')
plt.legend('labels')
plt.show()

# ------------------------------------------------------------------------------------------------------------------- #
# GeoEditors Dataset

file = r'C:\Users\MY LAPTOP\Downloads\geoeditors-monthly-2019-06.tsv'
hedars = ['Analytics', 'Data lake', 'Edits', 'Geoeditors', 'Public']
geo = pd.read_csv(file, header=None, index_col=False, names=hedars, delimiter="\t")

# plot 1
'''
This plot describes a scatter plot that shows the count of enwiki vs eswiki that happened in June, 2019.
'''
x = geo[geo['Analytics'] == 'enwiki']
y = geo[geo['Analytics'] == 'eswiki']
concat = pd.concat([x, y], ignore_index=True)
analytics = concat.Analytics.tolist()
wiki_region = {i: analytics.count(i) for i in analytics}
area = (30 * np.random.rand(len(wiki_region.values()))) ** 2
colors = np.random.rand(len(wiki_region.values()))
fig, ax = plt.subplots()
ax.plot(wiki_region.values(), wiki_region.keys())
ax.plot(wiki_region.values(), wiki_region.keys(), marker='^')
plt.title('Count of enwiki vs eswiki in June, 2019')
plt.xlabel('Count')
plt.ylabel('Countries')
plt.show()

# plot 2
'''
This plot describes a bar plot that shows the count of countries in oceania that got edited in June, 2019.
I took all the countries that had made edits in June, 2019.
'''
country = geo['Data lake'].tolist()
wiki_country = {i: country.count(i) for i in country}
oceania = [wiki_country['Australia'], wiki_country['Fiji'], wiki_country['Papua New Guinea'],
           wiki_country['New Zealand'], wiki_country['Palau'], wiki_country['Guam'], wiki_country['Marshall Islands'],
           wiki_country['New Caledonia'], wiki_country['Northern Mariana Islands']]
labels = ['Australia', 'Fiji', 'Papua New Guinea', 'New Zealand', 'Palau', 'Guam', 'Marshall Islands', 'New Caledonia',
          'Northern Mariana Islands']
colors = ['peru', 'm', 'b', 'violet', 'lightseagreen', 'olive', 'firebrick', 'darkcyan']

fig, ax = plt.subplots()
ax.barh(labels, oceania, color=colors)
ax.set_title('Count of countries in oceania that got edited in June, 2019')
ax.legend('labels')
ax.set_ylabel('Countries')
ax.set_xlabel('Counts')
plt.show()

# plot 3
'''
This plot describes a pie plot that shows the count of people how made edits in different Wikipedias in jordan,
in June, 2019.
I converted the two columns (analytics & edits) in a list and then drew the plot.
'''
edits = geo[geo['Data lake'] == 'Jordan']
analytics_Jordan = edits.Analytics.tolist()
geoedits_Jordan = edits.Geoeditors.tolist()
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
explode = [0, 0, 0.1, 0, 0]

fig, ax = plt.subplots()
ax.pie(geoedits_Jordan, explode=explode, labels=analytics_Jordan, autopct='%1.1f%%', startangle=90, shadow=True,
       colors=colors, textprops={'fontsize': 7})
ax.set_title('Active editors in Jordan')
ax.legend()

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.axis('equal')
plt.tight_layout()
plt.show()

# plot 4
'''
This plot describes a scatter plot that shows the most 25 countries that made edits in June, 2019.
I sorted the GeoEditor column in the dataframe and then took the least values
'''
upper_bound = geo.sort_values('Geoeditors').iloc[-25:]
labels = np.array(upper_bound['Data lake'])
max = np.array(upper_bound['Geoeditors'])
area = (3 * 7) ** 2
colors = np.random.rand(25)

fig, ax = plt.subplots()
ax.plot(max, labels, 'r--')
ax.scatter(max, labels, s=area, alpha=0.5, c=colors)
plt.ylabel('Geographic Edits ')
plt.xlabel('Countries')
plt.title('25 countries that made the highest edits in June, 2019')
plt.show()

# plot 5
'''
This plot describes a pie plot that shows the count of countries that made edits for 5 to 99 times or more than 100.
I counted the number of edits and then draw the plot
'''
edits = geo['Edits'].tolist()
x = {i: edits.count(i) for i in geo.Edits}
values = list(x.values())
s = [(values[0] + values[3]), (values[1] + values[2])]
labels = ['100 or more', '5 to 99']
explode = [0.0, 0.1]
colors = ['maroon', 'peru']

fig, ax = plt.subplots()
ax.pie(s, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90, )
ax.legend(loc='upper left')
ax.set_title('Edits that have been made in june of 2019')
plt.show()

# ------------------------------------------------------------------------------------------------------------------- #
# Unique Devices Dataset

# plot 1
'''
This plot describes a scatter plot that shows the relation between estimated and under estimated values 
((per domain )including the offset).
'''
plt.style.use('seaborn')

file = r'C:\Users\MY LAPTOP\Downloads\unique_devices_per_project_family_daily-2019-06-01.txt'
hedars = ['wikicountry', 'unest', 'est', 'offset']
data = pd.read_csv(file, header=None, index_col=False, names=hedars, delimiter="\t")

wikicountry = data['wikicountry']
unest = data['unest']
est = data['est']
offset = data['offset']

plt.scatter(est, unest, c=offset, cmap='summer', edgecolor='black', linewidth=1, alpha=0.75)
plt.xscale('log')
plt.yscale('log')
cbar = plt.colorbar()
cbar.set_label('offset values')
plt.legend()
plt.title('Wiki per Domain Relation')
plt.xlabel('Estimated ')
plt.ylabel('Und Estimated')
plt.tight_layout()
plt.show()

# plot 2
'''
This plot describes a plot that estimates all Wiktionary unique device visits 
(difference between under estimates and estimates values ).
'''
plt.plot(wikicountry, est, color='#444444', linestyle='--', label='estimates')
plt.plot(wikicountry, unest, label='under estimates ')
plt.fill_between(wikicountry, est, unest, where=(est > unest), interpolate=True, alpha=0.25, label='above Avg')
plt.fill_between(wikicountry, est, unest, where=(est <= unest), interpolate=True, color='red', alpha=0.25,
                 label='Below Avg')
plt.legend()
plt.title(" Estimate Values for All Wiktionary Unique Device Visits")
plt.xlabel('Wiki Projects ')
plt.ylabel('All Estimate Values')
plt.tight_layout()
plt.show()
