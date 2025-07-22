"use client"

import { useState } from "react"
import { UploadArea } from "@/components/upload-area"
import { WebsitePreview } from "@/components/website-preview"
import { parseFile, parseLinkedInUrl } from "@/lib/file-parser"
import type { ProfileData } from "@/types/profile"

export default function Home() {
  const [currentStep, setCurrentStep] = useState<"upload" | "preview">("upload")
  const [isUploading, setIsUploading] = useState(false)
  const [uploadProgress, setUploadProgress] = useState(0)
  const [profileData, setProfileData] = useState<ProfileData | null>(null)
  const [error, setError] = useState<string | null>(null)

  const simulateProgress = () => {
    setUploadProgress(0)
    const progressInterval = setInterval(() => {
      setUploadProgress((prev) => {
        if (prev >= 90) {
          clearInterval(progressInterval)
          return 90
        }
        return prev + Math.random() * 15
      })
    }, 300)
    return progressInterval
  }

  const handleFileUpload = async (file: File) => {
    setIsUploading(true)
    setError(null)

    const progressInterval = simulateProgress()

    try {
      const data = await parseFile(file)
      setProfileData(data)
      setUploadProgress(100)

      setTimeout(() => {
        setCurrentStep("preview")
        setIsUploading(false)
        setUploadProgress(0)
        clearInterval(progressInterval)
      }, 500)
    } catch (error) {
      console.error("Error parsing file:", error)
      setError(error instanceof Error ? error.message : "Failed to parse file")
      setIsUploading(false)
      setUploadProgress(0)
      clearInterval(progressInterval)
    }
  }

  const handleLinkedInUpload = async (url: string) => {
    setIsUploading(true)
    setError(null)

    const progressInterval = simulateProgress()

    try {
      const data = await parseLinkedInUrl(url)
      setProfileData(data)
      setUploadProgress(100)

      setTimeout(() => {
        setCurrentStep("preview")
        setIsUploading(false)
        setUploadProgress(0)
        clearInterval(progressInterval)
      }, 500)
    } catch (error) {
      console.error("Error parsing LinkedIn URL:", error)
      setError(error instanceof Error ? error.message : "Failed to parse LinkedIn profile")
      setIsUploading(false)
      setUploadProgress(0)
      clearInterval(progressInterval)
    }
  }

  const handleEdit = () => {
    setCurrentStep("upload")
    setProfileData(null)
    setError(null)
  }

  return (
    <div className="min-h-screen bg-white">
      {currentStep === "upload" ? (
        <div className="container mx-auto px-4 py-12">
          {/* Header */}
          <div className="text-center mb-12">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">Create Your Personal Website</h1>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Upload your LinkedIn profile export, resume, or provide your LinkedIn URL to instantly generate a modern,
              professional website that showcases your experience and skills.
            </p>
          </div>

          {/* Error Message */}
          {error && (
            <div className="max-w-2xl mx-auto mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-red-700 text-sm">{error}</p>
            </div>
          )}

          {/* Upload Area */}
          <UploadArea
            onFileUpload={handleFileUpload}
            onLinkedInUpload={handleLinkedInUpload}
            isUploading={isUploading}
            uploadProgress={uploadProgress}
          />

          {/* Features */}
          <div className="mt-16 grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div className="text-center space-y-3">
              <div className="w-12 h-12 bg-cyan-100 rounded-lg flex items-center justify-center mx-auto">
                <span className="text-2xl">🤖</span>
              </div>
              <h3 className="font-semibold text-gray-900">AI-Powered Parsing</h3>
              <p className="text-gray-600 text-sm">
                Advanced AI extracts and organizes your professional information automatically
              </p>
            </div>

            <div className="text-center space-y-3">
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mx-auto">
                <span className="text-2xl">✏️</span>
              </div>
              <h3 className="font-semibold text-gray-900">Fully Editable</h3>
              <p className="text-gray-600 text-sm">
                Edit any information inline after generation to perfect your website
              </p>
            </div>

            <div className="text-center space-y-3">
              <div className="w-12 h-12 bg-pink-100 rounded-lg flex items-center justify-center mx-auto">
                <span className="text-2xl">📱</span>
              </div>
              <h3 className="font-semibold text-gray-900">Professional Design</h3>
              <p className="text-gray-600 text-sm">Clean, modern layout that looks great on all devices</p>
            </div>
          </div>
        </div>
      ) : (
        <div className="min-h-screen">
          {profileData && <WebsitePreview profileData={profileData} onEdit={handleEdit} />}
        </div>
      )}
    </div>
  )
}
