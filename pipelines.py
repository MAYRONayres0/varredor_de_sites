# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

class sqllitePipeline(object):
    def open_spider(self, spider):
        self.connection=sqlite3.connect('apresentacoes.db')
        self.cursor=self.connection.cursor()
        # criar tabela
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS apresentacoes(
            show TEXT NOT NULL PRIMARY KEY,
            local TEXT,
            data TEXT
           
        )
                            ''')
        self.connection.commit()
    def close_spider(self,spider):
        self.connection.close()
    def process_item(self, item, spider):
        self.cursor.execute('''
                                INSERT OR IGNORE INTO apresentacoes(show, local, data) VALUES(?,?,?)
                            ''',(
                                item.get('show'),
                                item.get('local'),
                                item.get('data')
                            ))
        self.connection.commit()
        return item
