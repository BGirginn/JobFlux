interface Job {
  id: number;
  title: string;
  location: string;
  tags?: string[];
  salary_min?: number;
  salary_max?: number;
  description: string;
  company: string;
  url: string;
  created_at: string;
}

interface SearchParams {
  title?: string;
  location?: string;
  tags?: string;
  salary_min?: number;
  salary_max?: number;
}

export const searchJobs = async (params: SearchParams): Promise<Job[]> => {
  const query = new URLSearchParams(params as Record<string, string>).toString();
  const response = await fetch(`/api/v1/search?${query}`);
  if (!response.ok) {
    throw new Error('Failed to fetch jobs');
  }
  const data = await response.json();
  return data;
};
