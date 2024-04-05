import streamlit as st
import requests

def main():
    st.title(":rainbow[Select Tasks and Their Respective Percentages]")

    
    activities = [ "High level Gaming",
"Low level Gaming",
"Streaming 4k content",
"3D modeling",
"Video editing",
"Photo editing",
"Multi tasking",
"Programming (compiling large projects)",
"Web browsing",
"Basic MS Office tasks"
]
    
    activity_percentages = {}
    
    total_percentage = 0
    for activity in activities:
        max_percentage = min(100, 100 - total_percentage)
        if max_percentage > 0:
            percentage = st.slider(f"Percentage for {activity}", 0, max_percentage, 0, 5)
            activity_percentages[activity] = percentage
            total_percentage += percentage
        else:
            activity_percentages[activity] = 0
    
  #  st.write(":rainbow[Selected percentages:]")
  #  for activity, percentage in activity_percentages.items():
  #      st.write(f"- {activity}: {percentage}%")
    

####
        
    recommendations = {
    'High level Gaming': {
        'Asus': 40,
        'Acer': 30,
        'Dell': 20,
        'HP': 10,
        'Apple': 0
    },
    'Video rendering': {
        'Apple': 50,
        'Dell': 20,
        'HP': 15,
        'Asus': 10,
        'Acer': 5
    },
    'Machine learning training': {
        'Dell': 35,
        'Asus': 30,
        'Apple': 20,
        'HP': 10,
        'Acer': 5
    },
    'Streaming 4k content': {
        'Dell': 20,
        'Asus': 15,
        'HP': 15,
        'Apple': 40,
        'Acer': 10
    },
    'Low level Gaming': {
        'Acer': 35,
        'Asus': 30,
        'Dell': 20,
        'HP': 10,
        'Apple': 5
    },
    '3D modeling': {
        'HP': 30,
        'Dell': 25,
        'Asus': 20,
        'Acer': 15,
        'Apple': 10
    },
    'Video editing': {
        'Asus': 20,
        'Dell': 30,
        'Apple': 35,
        'HP': 10,
        'Acer': 5
    },
    'Photo editing': {
        'Apple': 45,
        'Dell': 25,
        'HP': 15,
        'Asus': 10,
        'Acer': 5
    },
    'Multi tasking': {
        'Dell': 25,
        'HP': 25,
        'Asus': 10,
        'Acer': 15,
        'Apple': 25
    },
    'Programming (compiling large projects)': {
        'Asus': 30,
        'Dell': 25,
        'HP': 20,
        'Acer': 15,
        'Apple': 10
    },
    'Web browsing': {
        'Apple': 40,
        'Dell': 30,
        'HP': 15,
        'Asus': 10,
        'Acer': 5
    },
    'Streaming (HD)': {
        'HP': 20,
        'Dell': 25,
        'Asus': 20,
        'Acer': 15,
        'Apple': 30
    },
    'Basic MS Office tasks': {
        'Acer': 25,
        'HP': 10,
        'Asus': 20,
        'Dell': 15,
        'Apple': 40
    },
    'Spreadsheet editing': {
        'Dell': 10,
        'HP': 25,
        'Acer': 20,
        'Asus': 15,
        'Apple': 30
    },
    'Email': {
        'Acer': 25,
        'Dell': 25,
        'HP': 15,
        'Asus': 15,
        'Apple': 20
    }
}


# processor
    processor=""
    for activity, requirement in activity_percentages.items():
        if requirement>0:
            if activity in ["High level Gaming","Video rendering","Machine learning training"]:
                processor="i7"
                break
            elif activity in ["Multi tasking","Streaming 4k content","Video editing","Photo editing","Programming (compiling large projects)","Streaming (4k)","3D modeling"]:
                processor="i5"
                break
            else:
                processor="i3"

####
    final = {}
    for activity, requirement in activity_percentages.items():
        if requirement > 0:
            for brand, value in recommendations[activity].items():
                if brand in final:
                    final[brand] += value * requirement
                else:
                    final[brand] = value * requirement
    for i in final:
        final[i]=final[i]/100
    sorted_final = dict(sorted(final.items(), key=lambda x: x[1], reverse=True))

    st.title(":rainbow[Laptop Recommended]")

    for i,j in sorted_final.items():
        if i=="Apple":
            st.write(f"{i} M1 : {j}%")
        else:
            st.write(f"{i} {processor} : {j}%")

####

if __name__ == "__main__":
    main()
