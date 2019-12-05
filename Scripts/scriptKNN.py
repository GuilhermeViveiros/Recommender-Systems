<?xml version="1.0" encoding="UTF-8"?>
<config xmlns="http://www.knime.org/2008/09/XMLConfig" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.knime.org/2008/09/XMLConfig http://www.knime.org/XMLConfig_2008_09.xsd" key="dialog">
<config key="internal_node_subsettings">
<entry key="memory_policy" type="xstring" value="CacheSmallInMemory"/>
</config>
<config key="model">
<entry key="sourceCode" type="xstring" value="import pandas as pd%%00010import numpy as np%%00010from sklearn.model_selection import train_test_split%%00010%%00010# Copy input to output%%00010ratings = input_table.copy()%%00010%%00010#split da data através do sklearn, UTILIZAR SAMPLING BIASES%%00010train,test = train_test_split(ratings, test_size = 0.2)%%00010%%00010#removo o que quero prever do x_train%%00010x_train = train.drop('rating', axis = 1);%%00010x_test = train['rating'];%%00010%%00010%%00010#removo o que quero prever do y_train%%00010y_train = test.drop('rating',axis=1);%%00010y_test = test['rating']%%00010%%00010%%00010%%00010#utilizo kNN, k-nearest-neighbor para ter os utilizadores mais%%00010#similares aos utilizadores que queremos prever%%00010"/>
<entry key="rowLimit" type="xint" value="1000"/>
<entry key="pythonVersionOption" type="xstring" value="python3"/>
<entry key="python2Command" type="xstring" value=""/>
<entry key="python3Command" type="xstring" value=""/>
<entry key="chunkSize" type="xint" value="500000"/>
<entry key="convertMissingToPython" type="xboolean" value="false"/>
<entry key="convertMissingFromPython" type="xboolean" value="false"/>
<entry key="sentinelOption" type="xstring" value="MIN_VAL"/>
<entry key="sentinelValue" type="xint" value="0"/>
</config>
</config>
