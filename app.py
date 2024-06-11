# import streamlit as st

# def main():
#     st.title('Formula 1 Chatbot')
#     st.write('Welcome to the Formula 1 Chatbot! Ask me anything about Formula 1.')

#     # Replace 'YOUR_BOTPRESS_URL' with your actual chatbot URL provided in your shareable link
#     botpress_url = 'https://mediafiles.botpress.cloud/a12e7caf-134a-4c19-ba5b-e5d2032ef516/webchat/bot.html'
    
#     # Embedding the chatbot iframe directly in the Streamlit app HTML template
#     iframe_html = f'<iframe src="{botpress_url}" width="100%" height="600" frameborder="0"></iframe>'
#     st.markdown(iframe_html, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()

import streamlit as st

def main():
    st.title('Formula 1 Chatbot')
    st.write('Welcome to the Formula 1 Chatbot! Ask me anything about Formula 1.')

    # Replace 'YOUR_BOTPRESS_URL' with the provided Botpress chatbot URL
    botpress_url = 'https://cdn.botpress.cloud/webchat/v2/shareable.html?botId=a12e7caf-134a-4c19-ba5b-e5d2032ef516'
    
    # Embedding the chatbot iframe directly in the Streamlit app HTML template
    iframe_html = f'<iframe src="{botpress_url}" width="100%" height="600" frameborder="0"></iframe>'
    st.markdown(iframe_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
