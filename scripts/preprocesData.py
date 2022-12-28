def preprocess(corpus)
    corpus_Encode=corpus.copy()
#La Base de datos ya se encuentra prepocesada en cuestion de repetidos y valores nulos o vacios
#se trasnforman los valores de texto en valores numericos mas estandar y personalizados teniendo en cuenta por ejemplo los meses que no aparecen
features = ['default' ,'housing', 'loan','month','day_of_week', 'y','contact','education','poutcome','marital','job']
feature_label_dict = {
                'default':{'unknown':0,'no':1,'yes':2},
                'housing':{'unknown':0,'no':1,'yes':2},
                'loan':{'unknown':0,'no':1,'yes':2},
                'month':{'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12},
                'day_of_week':{'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6,'sun':7},
                'y':{'no':0,'yes':1},
                'contact':{'unknown':0, 'cellular':1, 'telephone':2},
                'education':{'unknown':0,  'basic.4y':1,'basic.6y':2,'basic.9y':3,'high.school':4,'illiterate':5,'professional.course':6,'university.degree':7,},
                'poutcome':{'failure':1,'nonexistent':0,'success':2},
                'marital':{'unknown':0,'divorced':1,'single':2,'married':3},
                'job':{'unknown':0,'unemployed':1, 'student':2,'management':3, 'technician':4, 'entrepreneur':5, 'blue-collar':6, 'retired':7, 'admin.':8, 'services':9, 'self-employed':10, 'housemaid':11}
                 }
for f in features:     
  corpus_Encode = corpus_Encode.replace({f:feature_label_dict[f]})
  return corpus_Encode
