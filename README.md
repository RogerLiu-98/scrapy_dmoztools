# scrapy_dmoztools
### Basic Info
This is a spider written by scarpy that can crawl websites on [Dmoztools](http://dmoztools.net/), you can either specify the category you want or you can just set the paramter to null. In this case, the spider will automatically crawl every category on Dmoztools.
### How to use
* Download the source code:

`git clone https://github.com/RogerLiu-98/scrapy_dmoztools.git`

* Install requirements:

`pip install -r requirements.txt`

* Run the spider:

```
scrapy crawl dmoztools_spider

# Support category name:
# Arts
# Business
# Computers
# Games
# Health
# Home
# News
# Recreation
# Reference
# Regional
# Science
# Shopping
# Society
# Sports
# Kids_and_Teens
# World
scrapy crawl dmoztools_spider -a <category_name>
```