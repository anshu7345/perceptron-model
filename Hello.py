# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

import streamlit as st
import streamlit as st

class Perceptron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def predict(self, inputs):
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))
        return 1 if weighted_sum >= self.threshold else 0

weights = [0.7, 0.4, 0.6, 0.5, 0.3]
threshold = 1.8
perceptron = Perceptron(weights, threshold)

def main():
    st.title('Stock Investment Decision Maker')
    
    # Add image
    st.image('Stock-Market_BG.jpg', caption='Stock Market',width=500,align='center')

    st.write('Enter Criteria for Stock Investment Decision:')
    earnings = st.radio('Positive Earnings Report from the Company?', ('No', 'Yes'))
    trend = st.radio('Upward Market Trend?', ('No', 'Yes'))
    industry = st.radio('Company is in a Growing Industry?', ('No', 'Yes'))
    news = st.radio('Positive Recent News about the Company?', ('No', 'Yes'))
    recommendations = st.radio('The stock is Recommended by Analysts?', ('No', 'Yes'))

    inputs = [1 if val == 'Yes' else 0 for val in (earnings, trend, industry, news, recommendations)]

    if st.button('Make Decision'): 
        decision = perceptron.predict(inputs)
        result = 'Buy' if decision == 1 else 'Not buy'
        st.write(f'Decision: {result}')

if __name__ == '__main__':
    main()
