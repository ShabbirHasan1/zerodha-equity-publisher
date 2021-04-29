import axios from "axios";

export const fetchAllEquities = async () => {
  try {
    const { data } = await axios.get("/api/equities");

    if (!data) return [];

    const { equities, lastUpdated } = data;

    return {
      equities,
      lastUpdated,
    };
  } catch (err) {
    console.error(err);
  }
};

export const fetchEquitiesByName = async (name) => {
  try {
    if (!name) {
      const { equities } = await fetchAllEquities();
      return equities;
    } else {
      const { data } = await axios.get(`/api/equities/${name}`);
  
      if (!data) return [];
  
      return data;
    }
  } catch (err) {
    console.error(err);
  }
};

export const exportCsv = async (name) => {
  try {
    if (!name) {
      const { equities } = await fetchAllEquities();
      return equities;
    } else {
      const { data } = await axios.get(`/api/equities/export/${name ? name : ''}`);
  
      if (!data) return [];
  
      return data;
    }
  } catch (err) {
    console.error(err);
  }
}