select count(*) from mongodb.newsdb.news where regexp_like(title, 'Covid-19|کووید ۱۹|کویید ۱۹|کرونا|کروناویروس|سویه جدید') 
or regexp_like(summary, 'Covid-19|کووید ۱۹|کویید ۱۹|کرونا|کروناویروس|سویه جدید')
or regexp_like(text, 'Covid-19|کووید ۱۹|کویید ۱۹|کرونا|کروناویروس|سویه جدید')
or any_match(tags, t -> regexp_like(t, 'Covid-19|کووید ۱۹|کویید ۱۹|کرونا|کروناویروس|سویه جدید'));