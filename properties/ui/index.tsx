import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";

import { Property } from "./types";

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Render your React component instead
const root = createRoot(document.getElementById("reactapp"));

function App() {
  const [properties, setProperties] = useState([]);

  const s: string = "0";

  console.log("hello", s);

  useEffect(() => {
    fetch("/api", {
      method: "get",
      credentials: "same-origin",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        setProperties(data);
      })
      .catch(function (ex) {
        console.log("parsing failed", ex);
      });
  }, []);

  return (
    <div>
      {properties.map(({ address, value, city }: Property) => (
        <>
          <div>{address}</div>
          <div>{value}</div>
          <div>{city}</div>
        </>
      ))}
    </div>
  );
}

root.render(<App />);
