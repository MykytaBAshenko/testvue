<template>
    <div class="sidebarShell">
      <div @click="closeSidebar()" class="sidebarShellBG"></div>
      <div class="sidbar">
        <div class="sidbarHeader">
          <div>{{ forecastName }}</div>
          <button @click="closeSidebar()">X</button>
        </div>
        <div class="helpText">This Week</div>
  
        <div class="forecast-table">
          <!-- Loop through the forecast data for 7 days -->
          <div v-for="(day, index) in forecastData.time" :key="index" class="forecast-day">
            <div class="day-weathercode">
              <!-- You can also display an icon based on weather code if needed -->
              <NumberImage :numberImage="forecastData.weathercode[index]" />
            </div>
            <div class="day-date">{{ formatDate(day) }}</div>
            <div class="day-temperature">
                <div>
                <span>Max:</span> {{ forecastData.temperature_2m_max[index] }}°C 
            </div>
            <div>

              <span>Min:</span> {{ forecastData.temperature_2m_min[index] }}°C
            </div>
        </div>
        
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    forecastData: Object,
    toggleSidebar: Function,
    forecastName: String
  });
  
  // Close sidebar
  const closeSidebar = () => {
    props.toggleSidebar();
  };
  
  // Format date for display (optional, you can adjust the date format as needed)
  const formatDate = (date) => {
    const options = { weekday: 'short', day: 'numeric', month: 'short' };
    const formattedDate = new Date(date).toLocaleDateString(undefined, options);
    return formattedDate;
  };
  </script>
  
    
    <style scoped>
      .sidebarShellBG{
          background-color: black;
          opacity: 0.5;
          width: 100%;
          position: absolute;
          height: 100%;
          z-index: 5;
      }
      .sidebarShell{
          position: fixed;
          top: 0;
          z-index: 5;
          left: 0;
          display: grid;
          width: 100%;
          height: 100%;
      }
      .sidbar{
          z-index: 6;
          padding: 30px;
            height: 100%;      
            width: 100%;    
            justify-self: right;
            max-width: 600px;
          background-color: rgb(27, 27, 29);
      }
      .helpText{
        margin-bottom: 10px;
      }
      .sidbarHeader{
          display: grid;
          grid-template-columns: 1fr auto;
          margin-bottom: 10px;
          align-items: center;
          gap: 100px;
      }
      .sidbarHeader div{
          font-size: 30px;
          font-weight: 700;
      }
      .sidbarHeader button{
          font-weight: 700;
          width: 28px;
          height: 28px;
          display: grid;
          align-items: center;
          justify-content: center;       
          transition: 1s; 
          background-color: rgb(37,37,40);
      }
      .sidbarHeader button:hover{
          color: rgb(37,37,40);
          background-color: white;
      }
      .locationPopupModalInput input{
          font-size: 25px;
          padding-left:40px ;
  
      }
      .forecast-table{
        display: grid;
        grid-template-rows: auto;
        gap: 15px;
      }
      .forecast-day{
        background-color: rgb(50,50,50);
        border-radius: 15px;
        font-size: 25px;
        font-weight: 700;
        padding: 5px 25px;
        display: grid;
        align-items: center;
        gap: 20px;
        grid-template-columns: auto 1fr 1fr;
      }
      .day-weathercode svg{
        width: 50px;
        height: 50px;

      }
    </style>