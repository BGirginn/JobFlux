import React from 'react';

interface JobCardProps {
  title: string;
  company: string;
  location: string;
  description: string;
}

const JobCard: React.FC<JobCardProps> = ({ title, company, location, description }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md mb-4">
      <h2 className="text-xl font-bold mb-2">{title}</h2>
      <p className="text-gray-600 mb-1">{company} - {location}</p>
      <p className="text-gray-800">{description}</p>
    </div>
  );
};

export default JobCard;
