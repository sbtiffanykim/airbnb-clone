module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
  },
  purge: [],
  theme: {
    extend: {
      spacing: {
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
      },
      borderRadius: {
        xl: "1.5rem",
      },
      backgroundSize: {
        "1/2": "50%",
      },
    },
  },
  variants: {
    backgroundColor: ["responsive", "hover", "focus", "active"],
    backgroundSize: ["responsive", "hover", "focus", "active"],
  },
  plugins: [],
};
