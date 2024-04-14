import React from 'react';
import Image from 'next/image';
import heroImage from '@/assets/hero.webp';

const Hero = () => {
    return (
        <div className="bg-gray-900 py-20">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col-reverse md:flex-row items-center">
                <div className="md:w-1/2 space-y-6">
                    <h1 className="text-4xl font-bold text-white">
                        Welcome to Your App
                    </h1>
                    <p className="text-lg text-gray-400">
                        Discover the power of our app and transform the way you work.
                    </p>
                    <button className="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-6 rounded-md">
                        Get Started
                    </button>
                </div>
                <div className="md:w-1/2 mb-10 md:mb-0">
                    <Image
                        src={heroImage}
                        alt="Hero Image"
                        width={500}
                        height={400}
                        className="rounded-md shadow-lg"
                    />
                </div>
            </div>
        </div>
    );
};

export default Hero;