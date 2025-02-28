export default class ApiService {
    constructor(baseUrl) {
      this.baseUrl = baseUrl;
    }
  
    async getLocations() {
      try {
        const response = await useFetch(`${this.baseUrl}/locations`, {
          method: "GET"
        });
        return response.data.value;
      } catch (error) {
        console.error("GET request error:", error);
        throw error;
      }
    }
  
    async createLocation(name) {
      try {
        const response = await useFetch(`${this.baseUrl}/locations`, {
          method: "POST",
          body: { name },
        });
        return response.data.value;
      } catch (error) {
        console.error("POST request error:", error);
        throw error;
      }
    }

    async deleteLocation(id) {
        try {
          const response = await useFetch(`${this.baseUrl}/locations/${id}`, {
            method: "DELETE"
          });
          return response.data.value;
        } catch (error) {
          console.error("DELETE request error:", error);
          throw error;
        }
      }

    async forecast(id) {
      try {
        const response = await useFetch(`${this.baseUrl}/forecast/${id}`, {
          method: "GET"
        });
        return response.data.value;
      } catch (error) {
        console.error("GET request error:", error);
        throw error;
      }
    }
  }
  