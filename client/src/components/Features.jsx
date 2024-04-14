import React from 'react';

const Features = () => {
    return (
        <div className="bg-white py-20">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <h2 className="text-3xl font-bold text-gray-900 mb-10">
                    Features
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div className="bg-gray-100 rounded-md shadow-md p-6">
                        <h3 className="text-xl font-bold text-gray-900 mb-4">
                            Real-Time Leaderboards
                        </h3>
                        <p className="text-gray-600">
                            Stay up-to-date with the latest player rankings across
                            various sports, updated in real-time.
                        </p>
                    </div>
                    <div className="bg-gray-100 rounded-md shadow-md p-6">
                        <h3 className="text-xl font-bold text-gray-900 mb-4">
                            Player Profiles
                        </h3>
                        <p className="text-gray-600">
                            Explore detailed profiles of your favorite athletes,
                            including their stats, achievements, and highlights.
                        </p>
                    </div>
                    <div className="bg-gray-100 rounded-md shadow-md p-6">
                        <h3 className="text-xl font-bold text-gray-900 mb-4">
                            Customizable Tracking
                        </h3>
                        <p className="text-gray-600">
                            Set up personalized alerts and notifications to track
                            the progress of your chosen players and teams.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Features;