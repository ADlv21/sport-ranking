import React from 'react';
import Image from 'next/image';
import testimonialImage1 from '@/assets/user.png';

const Testimonials = () => {
    return (
        <div className="bg-gray-100 py-20">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <h2 className="text-3xl font-bold text-gray-900 mb-10">
                    Testimonials
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div className="bg-white rounded-md shadow-md p-6 flex">
                        <div className="mr-6">
                            <Image
                                src={testimonialImage1}
                                alt="Testimonial 1"
                                width={80}
                                height={80}
                                className="rounded-full"
                            />
                        </div>
                        <div>
                            <p className="text-gray-600 mb-4">
                                &quot;I absolutely love using this app. It has transformed
                                the way I work.&quot;
                            </p>
                            <h4 className="text-gray-900 font-bold">
                                John Doe
                            </h4>
                            <p className="text-gray-600">CEO, Acme Inc.</p>
                        </div>
                    </div>
                    <div className="bg-white rounded-md shadow-md p-6 flex">
                        <div className="mr-6">
                            <Image
                                src={testimonialImage1}
                                alt="Testimonial 2"
                                width={80}
                                height={80}
                                className="rounded-full"
                            />
                        </div>
                        <div>
                            <p className="text-gray-600 mb-4">
                                &quot;This app has been a game-changer for my business.
                                Highly recommended!&quot;
                            </p>
                            <h4 className="text-gray-900 font-bold">
                                Jane Smith
                            </h4>
                            <p className="text-gray-600">Founder, XYZ Corp.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Testimonials;