import React, { useState } from 'react';

// Accordion component
const Accordion = ({ items }) => {
  // State to track which accordion item is open
  const [openIndex, setOpenIndex] = useState(null);

  // Event handler to toggle accordion item visibility
  const handleAccordionClick = (index) => {
    // Toggle the index if it's already open, otherwise set it to the clicked index
    setOpenIndex((prevIndex) => (prevIndex === index ? null : index));
  };

  return (
    <div>
      {/* Map method through accordion items */}
      {items.map((item, index) => (
        <div key={index}>
          {/* Accordion title */}
          <div
            onClick={() => handleAccordionClick(index)}
            style={{
              cursor: 'pointer',
              padding: '10px',
              border: '1px solid #ddd',
              backgroundColor: openIndex === index ? '#f0f0f0' : 'white',
            }}
          >
            {item.title}
          </div>
          
          {/* Accordion body - conditionally render based on openIndex */}
          {openIndex === index && (
            <div style={{ padding: '10px', border: '1px solid #ddd' }}>
              {item.body}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default Accordion;
